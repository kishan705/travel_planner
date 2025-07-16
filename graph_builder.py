# graph_builder.py

import networkx as nx
from city_data import get_coordinates
from math import radians, sin, cos, sqrt, asin

def haversine(lat1, lon1, lat2, lon2):
    # great-circle distance in km
    lat1, lon1, lat2, lon2 = map(radians, (lat1, lon1, lat2, lon2))
    dlat, dlon = lat2-lat1, lon2-lon1
    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    return 6371 * 2 * asin(sqrt(a))

def build_graph(cities: list[str]) -> nx.Graph:
    """Complete graph: edges weighted by haversine distance."""
    G = nx.Graph()
    for city in cities:
        G.add_node(city)
    for i, c1 in enumerate(cities):
        lat1, lon1 = get_coordinates(c1)
        for c2 in cities[i+1:]:
            lat2, lon2 = get_coordinates(c2)
            dist = haversine(lat1, lon1, lat2, lon2)
            G.add_edge(c1, c2, weight=dist)
    return G

def find_shortest_path(G: nx.Graph, source: str, dest: str):
    """Return (path_list, total_distance_km) or (None, None)."""
    try:
        path = nx.dijkstra_path(G, source, dest, weight="weight")
        length = nx.dijkstra_path_length(G, source, dest, weight="weight")
        return path, length
    except nx.NetworkXNoPath:
        return None, None
