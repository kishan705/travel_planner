# map_visualizer.py

import folium
from city_data import get_coordinates

def plot_route(path: list[str], output_file="route_map.html"):
    """Generate and save an interactive map of the path."""
    # Extract lat/lon pairs
    coords = [get_coordinates(city) for city in path]
    # Center map on the first city
    m = folium.Map(location=coords[0], zoom_start=5)
    # Draw the path
    folium.PolyLine(locations=coords, color="blue", weight=4, opacity=0.7).add_to(m)
    # Markers
    folium.Marker(coords[0], popup="Start: "+path[0],
                  icon=folium.Icon(color="green")).add_to(m)
    folium.Marker(coords[-1], popup="End: "+path[-1],
                  icon=folium.Icon(color="red")).add_to(m)
    m.save(output_file)
    print(f"\n✅ Map saved as '{output_file}'. Open it in your browser!")
