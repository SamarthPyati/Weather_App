import requests
import json

city = "Bangalore"

BASE_URL = "http://api.weatherapi.com/v1/forecast.json"

data = {
    'key': "33c6bd00e41b40a7af052341232109",
    'q': city
}

response = requests.get(BASE_URL, params=data)

print(response.status_code)

try:
    if response.status_code == 200:
        weather_data = response.json()
        with open('data_json.json', 'w') as file:
            json.dump(weather_data, file, indent = 2)

except Exception as e:
    print(f"ERROR: {e}")
