
# ASN23 Downloader

Questo script automatizza il processo di download dei risultati ASN23 (Abilitazione Scientifica Nazionale, tornata 2023-2025) in base a parametri specificati. Estrae i dati dalle tabelle presenti sul sito e salva i file localmente, mantenendo i nomi corretti dei file come forniti dal server.

Si consiglia si utilizzarlo appena i risultati escono, in quanto dopo poco tempo vengono rimossi e non sono più accessibili. Si può utilizzare questo [repository](https://github.com/alessandropellegrini/risultati-asn) per controllare l'uscita del settore desiderato (eventualmente con servizi tipo [visualping](https://visualping.io/) per avere un alert.

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
- Per ogni candidato viene creata una cartella con il nome in questo formato: `<cognome>_<nome>_<abilitato>` dove`<abilitato>` è `Si/No`.
- Lo script mantiene i nomi originali dei file come specificati dal server.


## Contributi

I contributi sono benvenuti! Effettua un fork del repository e invia una pull request per eventuali correzioni di bug o nuove funzionalità.

## Licenza

Questo progetto è distribuito sotto la licenza Apache License 2.0. Consulta il file [LICENSE](LICENSE) per ulteriori dettagli.
