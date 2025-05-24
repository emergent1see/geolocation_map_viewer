# src/geolocation.py
import requests

def get_geolocation():
    try:
        response = requests.get("https://ipinfo.io/json")
        response.raise_for_status()
        data = response.json()

        loc = data.get("loc", "")
        latitude, longitude = map(float, loc.split(',')) if loc else (None, None)

        return {
            "ip": data.get("ip"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country"),
            "latitude": latitude,
            "longitude": longitude
        }
    except Exception as e:
        print(f"Error fetching geolocation: {e}")
        return None
