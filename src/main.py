# src/main.py
from geolocation import get_geolocation
from map_generator import generate_map

def main():
    geo = get_geolocation()
    if geo:
        print("Your Location Info:")
        print(f"IP: {geo['ip']}")
        print(f"City: {geo['city']}")
        print(f"Region: {geo['region']}")
        print(f"Country: {geo['country']}")
        print(f"Latitude: {geo['latitude']}")
        print(f"Longitude: {geo['longitude']}")
        generate_map(geo["latitude"], geo["longitude"], f"{geo['city']}, {geo['country']}")
    else:
        print("Could not determine location.")

if __name__ == "__main__":
    main()
