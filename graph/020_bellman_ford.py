def bellman_ford(graph, start):
    # Initialize distances from the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Relax edges up to (V - 1) times where V is the number of vertices
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    
    # Check for negative weight cycles
    for u in graph:
        for v, weight in graph[u]:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative weight cycle")
    
    return distances

# Example usage
if __name__ == "__main__":
    # Define the graph as an adjacency list with weights
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 5), ('D', 10)],
        'C': [('D', 3)],
        'D': []
    }
    
    # Run Bellman-Ford algorithm
    start_node = 'A'
    try:
        distances = bellman_ford(graph, start_node)
        
        # Print results
        print(f"Bellman-Ford Algorithm (starting from {start_node}):")
        for node, distance in distances.items():
            print(f"Distance to {node}: {distance}")
    except ValueError as e:
        print(e)
