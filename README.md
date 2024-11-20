
# ASN23 Downloader

Questo script automatizza il processo di download dei risultati ASN23 in base a parametri specificati. Estrae i dati dalle tabelle presenti sul sito e salva i file localmente, mantenendo i nomi corretti dei file come forniti dal server.

## Caratteristiche

- Scarica file in base a `settore`, `fascia` e `quadrimestre`.
- Gestisce URL relativi e assoluti.
- Determina automaticamente i nomi dei file dai messaggi di risposta del server.
- Organizza i file scaricati in directory create dinamicamente.

## Requisiti

- Python 3.7 o superiore
- Dipendenze:
  - `requests`
  - `beautifulsoup4`
  - `argparse`

Installa le dipendenze con:

```bash
pip install -r requirements.txt
```

## Utilizzo

Esegui lo script dalla riga di comando:

```bash
python asn23_downloader.py --settore "<SETTORE>" --fascia "<FASCIA>" --quadrimestre "<QUADRIMESTRE>"
```

### Argomenti

- `--settore`:  
  Il settore per il quale scaricare i file (ad esempio, `09/H1`).

- `--fascia`:  
  Il livello di fascia (ad esempio, `2`).

- `--quadrimestre`:  
  Il quadrimestre (ad esempio, `2`).

### Esempio

Per scaricare i file per `settore` `09/H1`, `fascia` `2` e `quadrimestre` `2`:

```bash
python asn23_downloader.py --settore "09/H1" --fascia "2" --quadrimestre "2"
```

### Output

- I file vengono salvati in una directory denominata `Quadrimestre_<QUADRIMESTRE>` (ad esempio, `Quadrimestre_2`).
- Lo script mantiene i nomi originali dei file come specificati dal server.

## Come Funziona

1. **Doppia Codifica**:  
   Il `settore` viene codificato due volte per soddisfare i requisiti URL del server.

2. **Costruzione Dinamica dell'URL**:  
   Lo script costruisce dinamicamente l'URL in base ai parametri forniti.

3. **Gestione di Content-Disposition**:  
   Se il server fornisce un'intestazione `Content-Disposition`, il nome del file viene estratto da questa.

4. **Elaborazione delle Tabelle**:  
   Le tabelle presenti sul sito vengono analizzate per identificare i link scaricabili.


## Contributi

I contributi sono benvenuti! Effettua un fork del repository e invia una pull request per eventuali correzioni di bug o nuove funzionalità.

## Licenza

Questo progetto è distribuito sotto la licenza Apache License 2.0. Consulta il file [LICENSE](LICENSE) per ulteriori dettagli.
