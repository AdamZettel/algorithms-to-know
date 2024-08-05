def kosaraju_scc(graph):
    # Helper function to perform DFS and track finishing times
    def dfs(v, visited, stack):
        visited.add(v)
        for neighbor in graph.get(v, []):
            if neighbor not in visited:
                dfs(neighbor, visited, stack)
        stack.append(v)
    
    # Helper function to transpose the graph
    def transpose_graph(graph):
        transposed = defaultdict(list)
        for v in graph:
            for neighbor in graph[v]:
                transposed[neighbor].append(v)
        return transposed

    # First pass: DFS to get the finishing times
    stack = []
    visited = set()
    for v in graph:
        if v not in visited:
            dfs(v, visited, stack)
    
    # Transpose the graph
    transposed = transpose_graph(graph)
    
    # Second pass: DFS on transposed graph
    visited.clear()
    sccs = []
    
    def dfs_transposed(v, visited, scc):
        visited.add(v)
        scc.append(v)
        for neighbor in transposed.get(v, []):
            if neighbor not in visited:
                dfs_transposed(neighbor, visited, scc)
    
    while stack:
        v = stack.pop()
        if v not in visited:
            scc = []
            dfs_transposed(v, visited, scc)
            sccs.append(scc)
    
    return sccs

# Example usage
if __name__ == "__main__":
    # Define the graph as an adjacency list
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A', 'D'],
        'D': ['E'],
        'E': ['F'],
        'F': ['D', 'G'],
        'G': ['H'],
        'H': ['G']
    }
    
    # Run Kosaraju's algorithm
    sccs = kosaraju_scc(graph)
    
    # Print the strongly connected components
    print("Strongly Connected Components:")
    for scc in sccs:
        print(" -> ".join(scc))
