import heapq
from collections import Counter, defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    # Calculate frequency of each character
    frequency = Counter(text)
    
    # Create a priority queue of nodes
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)
    
    # Build the Huffman Tree
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(priority_queue, merged)
    
    return priority_queue[0]

def generate_codes(node, prefix='', codebook=defaultdict()):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + '0', codebook)
        generate_codes(node.right, prefix + '1', codebook)
    return codebook

def huffman_encoding(text):
    root = build_huffman_tree(text)
    huffman_codes = generate_codes(root)
    encoded_text = ''.join(huffman_codes[char] for char in text)
    return encoded_text, huffman_codes

def huffman_decoding(encoded_text, huffman_codes):
    reverse_codes = {v: k for k, v in huffman_codes.items()}
    current_code = ''
    decoded_text = ''
    
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ''
    
    return decoded_text

# Example usage
if __name__ == "__main__":
    text = "this is an example for huffman encoding"
    
    # Encode the text
    encoded_text, huffman_codes = huffman_encoding(text)
    print("Encoded text:", encoded_text)
    print("Huffman Codes:", huffman_codes)
    
    # Decode the text
    decoded_text = huffman_decoding(encoded_text, huffman_codes)
    print("Decoded text:", decoded_text)
