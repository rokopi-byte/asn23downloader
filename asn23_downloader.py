import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import quote
import argparse


def download_file(file_url, file_path, session):
    """Download a file from the given URL to the specified file path."""
    try:
        print(f'Downloading {file_url}')
        file_response = session.get(file_url, stream=True)
        file_response.raise_for_status()  # Check for request errors

        content_disposition = file_response.headers.get('Content-Disposition')
        if content_disposition:
            match = re.search(r'filename="(.+)"', content_disposition)
            if match:
                file_name = match.group(1)
                file_path = os.path.join(os.path.dirname(file_path), file_name)

        with open(file_path, 'wb') as file:
            for chunk in file_response.iter_content(chunk_size=8192):  # Download in chunks
                file.write(chunk)
        print(f'Saved to {file_path}')
    except Exception as ex:
        print(f"Failed to download {file_url}: {ex}")


def process_table(table, download_dir, session, is_second_table=False):
    """Process a table, downloading files linked within."""
    base_url = 'https://asn23.cineca.it'  # Ensure the base URL is used for relative links
    for row in table.find_all('tr')[1:]:  # Skip the header row
        cells = row.find_all('td')
        if is_second_table and len(cells) > 2:  # Second table-specific processing
            folder_name = f"{cells[0].get_text(strip=True)}_{cells[1].get_text(strip=True)}_{cells[6].get_text(strip=True)}"
            folder_name = folder_name.replace(' ', '_')
            links = [cells[2].find('a', href=True), cells[3].find('a', href=True)]
        elif not is_second_table and len(cells) > 0:  # First table-specific processing
            folder_name = None
            links = [cells[0].find('a', href=True)]
        else:
            continue

        for link_tag in links:
            if link_tag:
                raw_file_url = link_tag['href']
                if not raw_file_url.startswith('http'):  # Fix for relative URLs
                    file_url = base_url + raw_file_url
                else:
                    file_url = raw_file_url

                if 'php' in file_url or 'indicatori' in file_url:
                    continue

                file_name = file_url.split('/')[-1]
                if '.' not in file_name:
                    file_name += '.pdf'

                subdir = os.path.join(download_dir, folder_name) if folder_name else download_dir
                os.makedirs(subdir, exist_ok=True)
                file_path = os.path.join(subdir, file_name)
                download_file(file_url, file_path, session)


def main():
    parser = argparse.ArgumentParser(description='Download files from ASN23 tables.')
    parser.add_argument('--settore', type=str, required=True, help='Settore (e.g., "09/H1")')
    parser.add_argument('--fascia', type=str, required=True, help='Fascia (e.g., "2")')
    parser.add_argument('--quadrimestre', type=str, required=True, help='Quadrimestre (e.g., "2")')
    args = parser.parse_args()

    # Replace `/` with `_` in settore
    cleaned_settore = args.settore.replace('/', '_')
    encoded_settore = quote(quote(args.settore, safe=''), safe='')

    base_url = 'https://asn23.cineca.it/pubblico/miur/esito'
    url = f'{base_url}/{encoded_settore}/{args.fascia}/{args.quadrimestre}'

    # Directory structure: settore -> quadrimestre -> fascia
    download_dir = os.path.join(cleaned_settore, f'Quadrimestre_{args.quadrimestre}', f'Fascia_{args.fascia}')
    os.makedirs(download_dir, exist_ok=True)

    session = requests.Session()

    response = session.get(url)
    response.raise_for_status()  # Check for request errors

    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all('table')

    if tables:
        process_table(tables[0], download_dir, session, is_second_table=False)
        if len(tables) > 1:
            process_table(tables[1], download_dir, session, is_second_table=True)

    print('Download complete.')


if __name__ == '__main__':
    main()
