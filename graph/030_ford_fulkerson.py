from collections import defaultdict

def dfs_capacity(graph, source, sink, parent, visited):
    # Mark the source node as visited
    visited.add(source)
    
    if source == sink:
        return True
    
    # Explore all adjacent nodes
    for neighbor, capacity in graph[source].items():
        if neighbor not in visited and capacity > 0:
            parent[neighbor] = source
            if dfs_capacity(graph, neighbor, sink, parent, visited):
                return True
    
    return False

def ford_fulkerson(graph, source, sink):
    # Initialize residual capacities
    residual_graph = defaultdict(lambda: defaultdict(int))
    for u in graph:
        for v, capacity in graph[u].items():
            residual_graph[u][v] = capacity
    
    parent = {}
    max_flow = 0
    
    while True:
        # Find an augmenting path using DFS
        visited = set()
        if not dfs_capacity(residual_graph, source, sink, parent, visited):
            break
        
        # Find the maximum flow through the path found by DFS
        path_flow = float('Inf')
        s = sink
        
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]
        
        # Update residual capacities of the edges and reverse edges
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]
        
        max_flow += path_flow
    
    return max_flow

# Example usage
if __name__ == "__main__":
    # Define the graph with capacities
    graph = defaultdict(lambda: defaultdict(int))
    
    # Add edges with capacities
    graph['s']['a'] = 10
    graph['s']['b'] = 5
    graph['a']['b'] = 15
    graph['a']['t'] = 10
    graph['b']['t'] = 10
    
    source = 's'
    sink = 't'
    
    # Run Ford-Fulkerson algorithm
    max_flow = ford_fulkerson(graph, source, sink)
    print(f"Maximum Flow: {max_flow}")
