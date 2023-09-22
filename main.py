import requests
import json

API_KEY_WEATHER = "581c975f755964037300e21b75805212"
API_KEY_AIR = "l3L65H6eG9QrX2dFB5SV3QbfKCknDcXx"


location = input("Location: ")
# coordinates = get_coordinates(location)

# BASE URL's
air_url = "https://api.meersens.com/environment/public"
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY_WEATHER}"

# ------------- WEATHER --------------

weather_response = requests.get(weather_url)

if weather_response.status_code == 200:
    weather_data = weather_response.json()
    with open('data/weather_data.json', 'w') as file:
        json.dump(weather_data, file, indent=2)

    temperature_celsius = round((weather_data['main']['temp'] - 273.15), 2)
    humidity = weather_data['main']['humidity']

    # Getting coordinates
    coordinates = (weather_data['coord']['lat'], weather_data['coord']['lon'])

    print(f"Weather in {location}:")
    print(f"Temperature: {temperature_celsius}°C")
    print(f"Humidity: {humidity}%")

    # ------------- AQI --------------

    air_quality_url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={coordinates[0]}&lon={coordinates[1]}&appid={API_KEY_WEATHER}'
    air_response = requests.get(air_quality_url)

    try:
        if air_response.status_code == 200:
            air_quality_data = air_response.json()
            with open('data/air_quality_data.json', 'w') as file:
                json.dump(air_quality_data, file, indent=2)

            # Extract AQI data
            aqi = air_quality_data['list'][0]['main']['aqi']

            print(f"Air Quality Index (AQI): {aqi}")
        else:
            print(f"Failed to retrieve air quality data. Status code: {air_response.status_code}")
    except Exception as e:
        print(e)

    # ------------- WQI --------------

    water_response = requests.get("https://api.meersens.com/environment/public/water/current", headers={
        'apikey': API_KEY_AIR
    }, params={
        'lat': coordinates[0],
        'lng': coordinates[1]
    })


    try:
        if water_response.status_code == 200:
            water_quality_data = water_response.json()
            with open('data/water_quality_json', 'w') as file:
                json.dump(water_quality_data, file, indent=2)

        else:
            print(f"Failed to retrieve water quality data. Status code: {water_response.status_code}")
    except Exception as e:
        print(e)
else:
    print(f"Failed to retrieve weather data. Status code: {weather_response.status_code}")
