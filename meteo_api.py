import datetime as dt
import requests

class Weather:
    
    # Classe responsabile per il recupero delle informazioni meteorologiche tramite l'API OpenWeatherMap.
    
    def __init__(self, api_key):
        # Inizializza l'oggetto con la chiave API e l'URL base per le richieste.
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather?"

    def fetch_weather(self, city):
       
    #Recupera i dati meteo per una specifica città tramite una richiesta API.
        
        url = f"{self.base_url}appid={self.api_key}&q={city}"
        response = requests.get(url).json()
        return response

    @staticmethod
    def kelvin_to_celsius_fahrenheit(kelvin):
        
    # Converte la temperatura da Kelvin a Celsius e Fahrenheit.
        
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9 / 5) + 32
        return celsius, fahrenheit

    @staticmethod
    def format_time(timestamp, timezone):
        
    #Converte un timestamp Unix in un formato leggibile, tenendo conto del fuso orario.
        
        return dt.datetime.utcfromtimestamp(timestamp + timezone).strftime('%Y-%m-%d %H:%M:%S')

class WeatherApp:
    
    # Classe principale per l'interazione con l'utente e la visualizzazione dei dati meteo.
    
    def __init__(self, api_key):
        # Inizializza l'app con un'istanza di Weather.
        self.weather_fetcher = Weather(api_key)

    def display_weather(self, city):
        
    # Recupera e mostra i dati meteo per una città specificata.
       
        data = self.weather_fetcher.fetch_weather(city)

        if data.get('cod') != 200:
            print(f"Errore: {data.get('message', 'Impossibile recuperare i dati')}")
            return

        # Estrai i dati principali dal JSON restituito.
        temp_kelvin = data['main']['temp']
        temp_celsius, temp_fahrenheit = self.weather_fetcher.kelvin_to_celsius_fahrenheit(temp_kelvin)

        feels_like_kelvin = data['main']['feels_like']
        feels_like_celsius, feels_like_fahrenheit = self.weather_fetcher.kelvin_to_celsius_fahrenheit(feels_like_kelvin)

        wind_speed = data['wind']['speed']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        sunrise_time = self.weather_fetcher.format_time(data['sys']['sunrise'], data['timezone'])
        sunset_time = self.weather_fetcher.format_time(data['sys']['sunset'], data['timezone'])

        date_time = dt.datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        # Mostra i dati meteo formattati.
        print("-----------------------------------------------------------------")
        print(f"Statistiche meteorologiche per - {city.upper()}  || {date_time}")
        print("-----------------------------------------------------------------")
        print(f"Temperatura attuale: {temp_celsius:.2f}°C, {temp_fahrenheit:.2f}°F")
        print(f"Percepita: {feels_like_celsius:.2f}°C, {feels_like_fahrenheit:.2f}°F")
        print(f"Descrizione(inglese): {description}")
        print(f"Umidità: {humidity}%")
        print(f"Velocità del vento: {wind_speed:.2f} m/s")
        print(f"Alba: {sunrise_time} ora locale")
        print(f"Tramonto: {sunset_time} ora locale")

if __name__ == "__main__":
    import config  # Assicurati che config.py contenga una variabile API_KEY

    # Recupera la chiave API da un modulo di configurazione.
    api_key = config.API_KEY

    if not api_key:
        print("Errore: chiave API non trovata. Assicurati di inserire una variabile APY_KEY nel file 'config.py'.")
        exit()

    # Inizializza l'app meteo.
    app = WeatherApp(api_key)

    # Ciclo principale per interagire con l'utente.
    while True:
        print("\nBenvenuto nell'app meteo!")
        print("1. Controlla il meteo di una città")
        print("2. Esci")

        scelta = input("Scegli un'opzione (1 o 2): ")

        if scelta == "1":
            city = input("Inserisci il nome della città: ")
            app.display_weather(city)
        elif scelta == "2":
            print("Grazie per aver usato l'app meteo. Arrivederci!")
            break
        else:
            print("Scelta non valida. Riprova.")

