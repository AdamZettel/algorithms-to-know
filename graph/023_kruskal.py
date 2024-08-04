class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(vertices, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Initialize union-find data structure
    uf = UnionFind(len(vertices))
    
    mst = []
    total_weight = 0
    
    for u, v, weight in edges:
        # Check if the current edge forms a cycle
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
            total_weight += weight
    
    return mst, total_weight

# Example usage
if __name__ == "__main__":
    # Define the graph as a list of edges (u, v, weight)
    edges = [
        (0, 1, 4),
        (0, 2, 2),
        (1, 2, 5),
        (1, 3, 10),
        (2, 3, 3)
    ]
    
    vertices = [0, 1, 2, 3]  # Example vertices
    
    # Run Kruskal's algorithm
    mst, total_weight = kruskal(vertices, edges)
    
    # Print results
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} - {v}: {weight}")
    print(f"Total weight of MST: {total_weight}")
