class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """Search for a word in the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        """Check if there is any word in the trie that starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage:
trie = Trie()
trie.insert("apple")
trie.insert("app")

print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: True
print(trie.search("appl"))   # Output: False
print(trie.starts_with("app"))  # Output: True
print(trie.starts_with("appl")) # Output: True
print(trie.starts_with("banana"))  # Output: False
