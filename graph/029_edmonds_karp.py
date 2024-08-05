from collections import deque, defaultdict

def bfs_capacity(graph, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)
    
    while queue:
        u = queue.popleft()
        
        for v, capacity in graph[u].items():
            if v not in visited and capacity > 0:  # Check if not visited and positive capacity
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
                queue.append(v)
    
    return False

def edmonds_karp(graph, source, sink):
    parent = {}
    max_flow = 0
    
    while bfs_capacity(graph, source, sink, parent):
        # Find the maximum flow through the path found by BFS
        path_flow = float('Inf')
        s = sink
        
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        
        # Update residual capacities of the edges and reverse edges
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
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
    
    # Run Edmonds-Karp algorithm
    max_flow = edmonds_karp(graph, source, sink)
    print(f"Maximum Flow: {max_flow}")
