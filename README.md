# progetto_natalizio🎅

# WeatherApp

WeatherApp è un'applicazione Python che permette agli utenti di controllare le condizioni meteo di una specifica città utilizzando l'API OpenWeatherMap.

## Funzionalità
- Recupero dei dati meteo in tempo reale per una città specificata.
- Conversione delle temperature da Kelvin a Celsius e Fahrenheit.
- Visualizzazione di dettagli come temperatura, umidità, descrizione del meteo, velocità del vento, orari di alba e tramonto.
- Interfaccia interattiva basata su terminale.

## Prerequisiti
### 1. Python
Assicurati di avere Python 3.7 o versioni successive installato. Verifica l'installazione con:
```bash
python --version
```

### 2. Chiave API di OpenWeatherMap
Registrati su [OpenWeatherMap](https://openweathermap.org/api) per ottenere la tua chiave API.

### 3. Moduli Python richiesti
Installa i moduli necessari utilizzando pip:
```bash
pip install requests
```

## Istruzioni per il Setup
### 1. Clona il Repository
Clona questo repository sul tuo computer locale:
```bash
git clone https://github.com/tuo-username/weather-app.git
cd weather-app
```

### 2. Configura la Chiave API
Crea un file `config.py` nella directory principale del progetto e aggiungi la tua chiave API:
```python
# config.py
API_KEY = "your_api_key"
```

In alternativa, puoi impostare la chiave API come variabile d'ambiente:
```bash
export API_KEY="your_api_key"
```

### 3. Esegui l'Applicazione
Esegui il programma utilizzando:
```bash
python main.py
```
Segui le istruzioni nel terminale per:
- Inserire il nome di una città e ottenere le informazioni meteo.
- Uscire dal programma selezionando l'opzione appropriata.

## Esempio di Utilizzo
```plaintext
Benvenuto nell'app meteo!
1. Controlla il meteo di una città
2. Esci

Scegli un'opzione (1 o 2): 1
Inserisci il nome della città: Roma
-----------------------------------------------------------------
Statistiche meteorologiche per - ROMA  || 09 Gen 2025 | 04:15:20 PM
-----------------------------------------------------------------
Temperatura attuale: 12.34°C, 54.21°F
Percepita: 10.56°C, 51.01°F
Descrizione (in inglese): cielo sereno
Umidità: 60%
Velocità del vento: 3.12 m/s
Alba: 2025-01-09 07:31:00 ora locale
Tramonto: 2025-01-09 17:05:00 ora locale
```

## Struttura del Codice
- **`Weather`**: Classe responsabile per il recupero e la formattazione dei dati dall'API OpenWeatherMap.
- **`WeatherApp`**: Classe principale che interagisce con l'utente e visualizza i dati meteo.
- **`main.py`**: Punto di ingresso per eseguire l'applicazione.

## Contributi
Contributi sono benvenuti! Sentiti libero di aprire un problema o inviare una pull request per miglioramenti o suggerimenti.

## Licenza
Questo progetto è distribuito sotto licenza MIT. Consulta il file `LICENSE` per ulteriori dettagli.

