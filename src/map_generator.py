# src/map_generator.py
import folium
import webbrowser
import os

def generate_map(latitude, longitude, location_info="You are here"):
    map_obj = folium.Map(location=[latitude, longitude], zoom_start=12)
    folium.Marker([latitude, longitude], popup=location_info).add_to(map_obj)

    map_file = "your_location_map.html"
    map_path = os.path.abspath(map_file)
    map_obj.save(map_path)
    webbrowser.open(f"file://{map_path}")
