import heapq

def prim(graph, start):
    # Priority queue to store edges (weight, vertex)
    min_heap = [(0, start)]
    mst_set = set()
    total_weight = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        
        if u in mst_set:
            continue
        
        # Add vertex to MST
        mst_set.add(u)
        total_weight += weight
        
        if weight > 0:
            mst_edges.append((prev_vertex, u, weight))
        
        # Explore neighbors
        for v, edge_weight in graph[u]:
            if v not in mst_set:
                heapq.heappush(min_heap, (edge_weight, v))
                prev_vertex = u

    return mst_edges, total_weight

# Example usage
if __name__ == "__main__":
    # Define the graph as an adjacency list with weights
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 5), ('D', 10)],
        'C': [('A', 2), ('B', 5), ('D', 3)],
        'D': [('B', 10), ('C', 3)]
    }
    
    # Run Prim's algorithm
    start_node = 'A'
    mst_edges, total_weight = prim(graph, start_node)
    
    # Print results
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst_edges:
        print(f"{u} - {v}: {weight}")
    print(f"Total weight of MST: {total_weight}")
