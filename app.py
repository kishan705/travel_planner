from flask import Flask, render_template, request, jsonify
# This imports your existing Dijkstra's logic
import graph_logic 

app = Flask(__name__)

# IMPORTANT: Replace this with the actual dictionary of coordinates from your project.
# The keys (like 'A', 'B') must match the node names in your graph.
NODE_COORDINATES = {
    'A': (25.3176, 82.9739), # Varanasi
    'B': (25.4358, 81.8463), # Prayagraj
    'C': (26.4499, 80.3319), # Kanpur
    'D': (26.8467, 80.9462), # Lucknow
    'E': (27.1767, 78.0081)  # Agra
}

@app.route('/')
def index():
    """Serves the main HTML page."""
    return render_template('index.html')

@app.route('/calculate_route', methods=['POST'])
def calculate_route():
    """API endpoint to calculate the shortest route."""
    data = request.get_json()
    start_node = data.get('start')
    end_node = data.get('end')

    if not start_node or not end_node:
        return jsonify({'error': 'Start and end nodes are required'}), 400

    try:
        # IMPORTANT: Make sure this function call matches your code.
        # It should take a start and end node and return a list of nodes in the path.
        path = graph_logic.find_shortest_path(start_node, end_node)

        if not path:
            return jsonify({'error': 'No path found'}), 404

        # Convert the path of node names to a list of [lat, lon] coordinates
        route_coordinates = [NODE_COORDINATES[node] for node in path]

        return jsonify({'route': route_coordinates})

    except KeyError as e:
        return jsonify({'error': f'Invalid node name: {e}'}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
