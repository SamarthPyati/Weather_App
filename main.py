import requests
import json

city = "Bangalore"

BASE_URL = "http://api.weatherapi.com/v1"

weather_data = {
    'key': "33c6bd00e41b40a7af052341232109",
    'q': city,
}

air_data = {
    'key': "33c6bd00e41b40a7af052341232109",
    'q': city,
    'aqi':'yes'
}

weather_response = requests.get(f"{BASE_URL}/forecast.api", params=weather_data)
air_response = requests.get(f"{BASE_URL}/current/airquality", params=air_data)
# print(response.status_code)

try:
    if weather_response.status_code == 200:
        weather_data = weather_response.json()
        with open('weather_data.json', 'w') as file:
            json.dump(weather_data, file, indent = 2)

except Exception as e:
    print(f"ERROR (WEATHER): {e}")

try:
    if air_response.status_code == 200:
        air_data = air_response.json()
        with open('air_data.json', 'w') as file:
            json.dump(air_data, file, indent = 2)
except Exception as e:
    print(f"ERROR (AIR_DATA): {e}")
