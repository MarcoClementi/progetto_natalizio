```Mermaid
classDiagram
    class Weather {
        -api_key-->str
        -base_url-->str
        +__init__(api_key: str)
        +fetch_weather(city: str)-->dict
        +kelvin_to_celsius_fahrenheit(kelvin: float):
        +format_time(timestamp: int, timezone: int)--> str
    }

    class WeatherApp {
        -weather_fetcher: Weather
        +__init__(api_key: str)
        +display_weather(city: str)-->void
    }

    WeatherApp --> Weather : Utilizza
