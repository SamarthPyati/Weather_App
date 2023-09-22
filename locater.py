from geopy.geocoders import Nominatim


def get_coordinates(location: str):
    geolocator = Nominatim(user_agent="geocoder")
    location_data = geolocator.geocode(location)

    if location_data:
        return (location_data.latitude, location_data.longitude)
    else:
        print("Location not found.")

if __name__ == "__main__":
    print(get_coordinates("Bangalore"))