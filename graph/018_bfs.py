from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        while queue:
            node = queue.popleft()
            print(node, end=' ')
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
    def dfs_recursive(self, node, visited):
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbor in self.graph[node]:
                self.dfs_recursive(neighbor, visited)
    
    def dfs_stack(self, start):
        visited = set()
        stack = [start]
        
        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                stack.extend(neighbor for neighbor in self.graph[node] if neighbor not in visited)
    
    def print_graph(self):
        for node in self.graph:
            print(f"{node}: {', '.join(map(str, self.graph[node]))}")

# Example usage
if __name__ == "__main__":
    g = Graph()
    
    # Add edges to the graph
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('C', 'G')
    
    # Print the graph
    print("Graph Representation:")
    g.print_graph()
    
    # Perform BFS
    print("\nBFS Traversal:")
    g.bfs('A')
    
    # Perform DFS using recursion
    print("\n\nDFS Recursive Traversal:")
    visited_recursive = set()
    g.dfs_recursive('A', visited_recursive)
    
    # Perform DFS using a stack
    print("\n\nDFS Stack Traversal:")
    g.dfs_stack('A')
