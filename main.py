# main.py

from city_data import validate_city
from graph_builder import build_graph, find_shortest_path
from map_visualizer import plot_route

def main():
    print("Enter cities (comma‑separated). Any world city is allowed:")
    raw = input().strip().split(",")
    cities = [c.strip() for c in raw]

    # Validate
    valid = []
    for c in cities:
        if validate_city(c):
            valid.append(c)
        else:
            print(f"⚠ '{c}' not found in database; skipping.")
    if len(valid) < 2:
        print("❌ Need at least two valid cities—exiting.")
        return

    print("\n✅ Valid cities:", ", ".join(valid))
    print("Building graph and computing shortest routes...")

    G = build_graph(valid)

    src = input("\nEnter source city:\n").strip()
    dst = input("Enter destination city:\n").strip()
    if src not in G or dst not in G:
        print("❌ Source or destination not among the validated cities.")
        return

    path, dist = find_shortest_path(G, src, dst)
    if not path:
        print("❌ No path found.")
        return

    print("\nBest route:", " -> ".join(path))
    print(f"Total distance: {dist:.2f} km")
    plot_route(path)

if __name__ == "__main__":
    main()
