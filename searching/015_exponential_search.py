def exponential_search(arr, target):
    n = len(arr)
    
    # Check if the target is present at the first index
    if arr[0] == target:
        return 0
    
    # Find the range where the target might be
    index = 1
    while index < n and arr[index] <= target:
        index *= 2
    
    # Perform binary search within the found range
    low = index // 2
    high = min(index, n - 1)
    
    return binary_search(arr, low, high, target)

def binary_search(arr, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 4, 5, 7, 9, 12, 15, 18, 21]
    target = 15
    result = exponential_search(arr, target)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")
