from flask import Flask, render_template, request, jsonify
# Import your specific functions and data
from graph_logic import build_graph, find_shortest_path
from city_data import CITIES, get_coordinates # Assumes city_data.py has a CITIES list

app = Flask(__name__)

# --- Build the Graph and Coordinates Dictionary on Startup ---
print("Building city graph...")
CITY_GRAPH = build_graph(CITIES) # Create the graph object
print("Graph built successfully!")

# Create a dictionary of coordinates for the frontend to use
NODE_COORDINATES = {city: get_coordinates(city) for city in CITIES}
# -------------------------------------------------------------

@app.route('/')
def index():
    """Serves the main HTML page."""
    return render_template('index.html')

@app.route('/calculate_route', methods=['POST'])
def calculate_route():
    """API endpoint that uses your Dijkstra's algorithm."""
    data = request.get_json()
    start_node = data.get('start')
    end_node = data.get('end')

    if not start_node or not end_node:
        return jsonify({'error': 'Start and end nodes are required'}), 400

    try:
        # Use your find_shortest_path function with the pre-built graph
        path, length = find_shortest_path(CITY_GRAPH, start_node, end_node)

        if not path:
            return jsonify({'error': 'No path found between the specified nodes'}), 404

        # Convert the list of city names into a list of [lat, lon] coordinates
        route_coordinates = [NODE_COORDINATES[city] for city in path]

        # Return the coordinates and total distance
        return jsonify({
            'route': route_coordinates,
            'distance_km': round(length, 2)
        })

    except KeyError as e:
        # This handles cases where the user enters a city not in your list
        return jsonify({'error': f'Invalid city name: {e}. Please use a valid city from the list.'}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
