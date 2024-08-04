def floyd_warshall(graph):
    # Initialize distance matrix
    nodes = list(graph.keys())
    distance = {node: {node2: float('inf') for node2 in nodes} for node in nodes}
    
    # Set distance to self as 0
    for node in nodes:
        distance[node][node] = 0
    
    # Set distances based on the graph edges
    for u in graph:
        for v, weight in graph[u]:
            distance[u][v] = weight
    
    # Floyd-Warshall algorithm
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    
    return distance

# Example usage
if __name__ == "__main__":
    # Define the graph as an adjacency list with weights
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 5), ('D', 10)],
        'C': [('D', 3)],
        'D': []
    }
    
    # Run Floyd-Warshall algorithm
    distances = floyd_warshall(graph)
    
    # Print results
    print("Floyd-Warshall Algorithm (shortest path distances):")
    for i in distances:
        for j in distances[i]:
            print(f"Distance from {i} to {j}: {distances[i][j]}")
