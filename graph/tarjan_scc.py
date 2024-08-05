def tarjan_scc(graph):
    index = 0
    stack = []
    on_stack = set()
    indices = {}
    low_link = {}
    sccs = []

    def strongconnect(v):
        nonlocal index
        indices[v] = index
        low_link[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)

        # Consider successors of v
        for w in graph.get(v, []):
            if w not in indices:
                # Successor w has not yet been visited; recurse on it
                strongconnect(w)
                low_link[v] = min(low_link[v], low_link[w])
            elif w in on_stack:
                # Successor w is in stack and hence in the current SCC
                low_link[v] = min(low_link[v], indices[w])

        # If v is a root node, pop the stack and generate an SCC
        if low_link[v] == indices[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    # Start the DFS traversal for each vertex
    for v in graph:
        if v not in indices:
            strongconnect(v)
    
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
    
    # Run Tarjan's algorithm
    sccs = tarjan_scc(graph)
    
    # Print the strongly connected components
    print("Strongly Connected Components:")
    for scc in sccs:
        print(" -> ".join(scc))
