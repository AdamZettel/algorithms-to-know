import heapq

def dijkstra(graph, start):
    # Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, node)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Skip if this distance is not the shortest known distance
        if current_distance > distances[current_node]:
            continue
        
        # Process each neighbor
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # Only update if the new distance is shorter
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
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
    
    # Run Dijkstra's algorithm
    start_node = 'A'
    distances = dijkstra(graph, start_node)
    
    # Print results
    print(f"Dijkstra's Algorithm (starting from {start_node}):")
    for node, distance in distances.items():
        print(f"Distance to {node}: {distance}")
