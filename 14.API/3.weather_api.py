import requests
from dotenv import load_dotenv
import os


load_dotenv()

OWM_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')

url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'q': 'Seoul',
    'appid': OWM_API_KEY,
    'units': 'metric',
    'lang': 'en'
}

response = requests.get(url, params=params)
response.raise_for_status()

weather_data = response.json()
city_name = weather_data['name']
temperature = weather_data['main']['temp']
description = weather_data['weather'][0]['description']

print(f'도시: {city_name}')
print(f'온도: {temperature}')
print(f'날씨: {description}')
