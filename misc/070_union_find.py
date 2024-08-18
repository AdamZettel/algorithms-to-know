class UnionFind:
    def __init__(self, size):
        # Initialize the parent array where each element is its own parent (self-loop)
        self.parent = list(range(size))
        # Initialize the rank array to keep track of the depth of trees
        self.rank = [1] * size

    def find(self, p):
        """Find the representative of the set containing element p with path compression."""
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        """Union the sets containing elements p and q."""
        rootP = self.find(p)
        rootQ = self.find(q)
        
        if rootP != rootQ:
            # Union by rank: attach the smaller tree under the larger tree
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

    def connected(self, p, q):
        """Check if elements p and q are in the same set."""
        return self.find(p) == self.find(q)

# Example usage
if __name__ == "__main__":
    uf = UnionFind(10)  # Create a UnionFind with 10 elements (0 to 9)
    
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(4, 5)
    
    print(uf.connected(1, 3))  # Output: True
    print(uf.connected(1, 4))  # Output: False
    
    uf.union(3, 4)
    print(uf.connected(1, 4))  # Output: True
