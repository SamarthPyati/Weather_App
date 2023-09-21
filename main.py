import requests
import json

API_KEY = "581c975f755964037300e21b75805212"   

location = "Delhi"

weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"

response = requests.get(weather_url)

if response.status_code == 200:
    weather_data = response.json()
    with open('weather_data.json', 'w') as file:
        json.dump(weather_data, file, indent = 2)

    temperature_celsius = round((weather_data['main']['temp'] - 273.15), 2)
    humidity = weather_data['main']['humidity']

    print(f"Weather in {location}:")
    print(f"Temperature: {temperature_celsius}°C")
    print(f"Humidity: {humidity}%")

    air_quality_url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={weather_data["coord"]["lat"]}&lon={weather_data["coord"]["lon"]}&appid={API_KEY}'

    # Send a GET request to retrieve air quality data
    response = requests.get(air_quality_url)

    if response.status_code == 200:
        air_quality_data = response.json()
        with open('air_quality_data.json', 'w') as file:
            json.dump(air_quality_data, file, indent = 2)
        
        # Extract AQI data
        aqi = air_quality_data['list'][0]['main']['aqi']

        print(f"Air Quality Index (AQI): {aqi}")
    else:
        print(f"Failed to retrieve air quality data. Status code: {response.status_code}")

else:
    print(f"Failed to retrieve weather data. Status code: {response.status_code}")
