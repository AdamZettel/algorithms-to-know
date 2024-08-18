class SuffixTreeNode:
    def __init__(self, start, end):
        self.children = {}
        self.start = start
        self.end = end
        self.suffix_link = None

class SuffixTree:
    def __init__(self, text):
        self.text = text
        self.root = SuffixTreeNode(None, None)
        self.build_suffix_tree()

    def build_suffix_tree(self):
        """Build the suffix tree for the given text."""
        n = len(self.text)
        for i in range(n):
            self.insert_suffix(i)

    def insert_suffix(self, start_index):
        """Insert a suffix starting at start_index into the suffix tree."""
        current_node = self.root
        suffix = self.text[start_index:]
        while suffix:
            if suffix[0] in current_node.children:
                edge_start, edge_end = current_node.children[suffix[0]].start, current_node.children[suffix[0]].end
                edge_label = self.text[edge_start:edge_end]
                i = 0
                while i < len(edge_label) and i < len(suffix) and edge_label[i] == suffix[i]:
                    i += 1
                
                if i == len(edge_label):
                    current_node = current_node.children[suffix[0]]
                    suffix = suffix[i:]
                else:
                    split_node = SuffixTreeNode(edge_start, edge_start + i)
                    current_node.children[edge_label[0]] = split_node
                    child = current_node.children.pop(suffix[0])
                    split_node.children[edge_label[i]] = child
                    child.start += i
                    split_node.children[suffix[i]] = SuffixTreeNode(start_index, n)
                    suffix = ""
            else:
                current_node.children[suffix[0]] = SuffixTreeNode(start_index, n)
                suffix = ""

    def print_tree(self, node=None, indent=""):
        """Print the suffix tree."""
        if node is None:
            node = self.root
        for child in node.children.values():
            edge_label = self.text[child.start:child.end]
            print(indent + edge_label)
            self.print_tree(child, indent + "  ")

# Example usage:
text = "banana"
suffix_tree = SuffixTree(text)
suffix_tree.print_tree()
