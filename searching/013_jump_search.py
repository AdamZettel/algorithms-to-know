import math

def jump_search(arr, target):
    n = len(arr)
    # Find the block size to jump
    step = int(math.sqrt(n))
    prev = 0
    
    # Jump ahead by step size
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Linear search within the block
    for idx in range(prev, min(step, n)):
        if arr[idx] == target:
            return idx
    
    return -1

# Example usage
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 15
    result = jump_search(arr, target)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")
