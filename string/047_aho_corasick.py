from collections import deque, defaultdict

class AhoCorasick:
    def __init__(self):
        self.num_nodes = 1
        self.edges = [{}]
        self.fail = [-1]
        self.output = [set()]

    def add_pattern(self, pattern, index):
        """Add a pattern to the trie."""
        current_node = 0
        for char in pattern:
            if char not in self.edges[current_node]:
                self.edges[current_node][char] = self.num_nodes
                self.edges.append({})
                self.fail.append(-1)
                self.output.append(set())
                self.num_nodes += 1
            current_node = self.edges[current_node][char]
        self.output[current_node].add(index)

    def build_failure_links(self):
        """Build the failure links using BFS."""
        queue = deque()
        
        for char in self.edges[0]:
            node = self.edges[0][char]
            self.fail[node] = 0
            queue.append(node)

        while queue:
            r = queue.popleft()

            for char, u in self.edges[r].items():
                queue.append(u)
                state = self.fail[r]

                while state != -1 and char not in self.edges[state]:
                    state = self.fail[state]
                
                if state == -1:
                    self.fail[u] = 0
                else:
                    self.fail[u] = self.edges[state][char]
                    self.output[u].update(self.output[self.fail[u]])

    def search(self, text):
        """Search for patterns in the text."""
        current_node = 0
        results = []

        for i, char in enumerate(text):
            while current_node != -1 and char not in self.edges[current_node]:
                current_node = self.fail[current_node]
            
            if current_node == -1:
                current_node = 0
                continue
            
            current_node = self.edges[current_node][char]
            
            if self.output[current_node]:
                for pattern_index in self.output[current_node]:
                    results.append((i, pattern_index))
        
        return results

# Example usage:
patterns = ["he", "she", "his", "hers"]
text = "ushers"

ac = AhoCorasick()
for i, pattern in enumerate(patterns):
    ac.add_pattern(pattern, i)

ac.build_failure_links()
matches = ac.search(text)

# Display matches
for position, pattern_index in matches:
    print(f"Pattern '{patterns[pattern_index]}' found at index {position - len(patterns[pattern_index]) + 1}")
