import heapq
from collections import defaultdict, deque

def bellman_ford(graph, source):
    # Initialize distances from source to all vertices as infinity
    distances = defaultdict(lambda: float('inf'))
    distances[source] = 0
    vertices = list(graph.keys())

    # Relax edges up to V-1 times
    for _ in range(len(vertices) - 1):
        for u in vertices:
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    
    # Check for negative-weight cycles
    for u in vertices:
        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative weight cycle")
    
    return distances

def dijkstra(graph, start):
    # Initialize distances and priority queue
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)
        
        if current_distance > distances[u]:
            continue
        
        for v, weight in graph[u]:
            distance = current_distance + weight
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(priority_queue, (distance, v))
    
    return distances

def johnson(graph):
    # Step 1: Add a new vertex `q` connected to all other vertices with zero-weight edges
    new_vertex = 'q'
    new_graph = defaultdict(list, {u: edges[:] for u, edges in graph.items()})
    
    for u in graph:
        new_graph[new_vertex].append((u, 0))
    
    # Step 2: Run Bellman-Ford algorithm from the new vertex
    h = bellman_ford(new_graph, new_vertex)
    
    # Step 3: Re-weight the original graph
    reweighted_graph = defaultdict(list)
    for u in graph:
        for v, weight in graph[u]:
            new_weight = weight + h[u] - h[v]
            reweighted_graph[u].append((v, new_weight))
    
    # Step 4: Run Dijkstra's algorithm for each vertex in the re-weighted graph
    all_pairs_shortest_paths = {}
    for u in graph:
        all_pairs_shortest_paths[u] = dijkstra(reweighted_graph, u)
    
    # Adjust distances back to original weights
    for u in all_pairs_shortest_paths:
        for v in all_pairs_shortest_paths[u]:
            all_pairs_shortest_paths[u][v] += h[v] - h[u]
    
    return all_pairs_shortest_paths

# Example usage
if __name__ == "__main__":
    # Define the graph as an adjacency list
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    
    # Run Johnson's algorithm
    try:
        shortest_paths = johnson(graph)
        print("All pairs shortest paths:")
        for u in shortest_paths:
            print(f"From {u}:")
            for v in shortest_paths[u]:
                print(f"  To {v}: {shortest_paths[u][v]}")
    except ValueError as e:
        print(e)
