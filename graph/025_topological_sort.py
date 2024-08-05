from collections import deque, defaultdict

# Kahn's Algorithm for Topological Sort
def topological_sort_kahn(graph):
    # Compute in-degrees of all nodes
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # Initialize the queue with nodes having 0 in-degree
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    topological_order = []
    
    while queue:
        node = queue.popleft()
        topological_order.append(node)
        
        # Decrease the in-degree of neighbors
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if topological sort is possible (i.e., if graph is a DAG)
    if len(topological_order) == len(graph):
        return topological_order
    else:
        raise ValueError("Graph is not a DAG (contains a cycle)")

# DFS-Based Algorithm for Topological Sort
def topological_sort_dfs(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)
    
    # Perform DFS from each node
    for node in graph:
        if node not in visited:
            dfs(node)
    
    # The stack contains the topological order in reverse
    return stack[::-1]

# Combined Script
if __name__ == "__main__":
    # Define the graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': ['E'],
        'E': []
    }
    
    # Run Kahn's algorithm
    try:
        topo_order_kahn = topological_sort_kahn(graph)
        print("Topological Sort (Kahn's Algorithm):")
        print(" -> ".join(topo_order_kahn))
    except ValueError as e:
        print(e)
    
    # Run DFS-based algorithm
    topo_order_dfs = topological_sort_dfs(graph)
    print("Topological Sort (DFS-Based Algorithm):")
    print(" -> ".join(topo_order_dfs))
