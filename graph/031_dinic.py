from collections import deque, defaultdict

def bfs_level_graph(graph, source, sink, level):
    # Initialize the level graph
    for node in graph:
        level[node] = -1
    level[source] = 0
    
    queue = deque([source])
    
    while queue:
        u = queue.popleft()
        
        for v, capacity in graph[u].items():
            if level[v] < 0 and capacity > 0:  # Not visited and has residual capacity
                level[v] = level[u] + 1
                if v == sink:
                    return True
                queue.append(v)
    
    return False

def dfs_blocking_flow(graph, u, sink, flow, level, start):
    if u == sink:
        return flow
    
    while start[u] < len(graph[u]):
        v, capacity = graph[u][list(graph[u])[start[u]]]
        if level[v] == level[u] + 1 and capacity > 0:
            current_flow = min(flow, capacity)
            temp_flow = dfs_blocking_flow(graph, v, sink, current_flow, level, start)
            
            if temp_flow > 0:
                graph[u][v] -= temp_flow
                graph[v][u] += temp_flow
                return temp_flow
        
        start[u] += 1
    
    return 0

def dinic(graph, source, sink):
    total_flow = 0
    level = {}
    
    while bfs_level_graph(graph, source, sink, level):
        start = {node: 0 for node in graph}
        while True:
            flow = dfs_blocking_flow(graph, source, sink, float('Inf'), level, start)
            if flow == 0:
                break
            total_flow += flow
    
    return total_flow

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
    
    # Run Dinic's algorithm
    max_flow = dinic(graph, source, sink)
    print(f"Maximum Flow: {max_flow}")
