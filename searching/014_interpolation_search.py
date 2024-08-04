def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high and target >= arr[low] and target <= arr[high]:
        # Estimate the position of the target value
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))
        
        # Check if the estimated position is the target
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    
    return -1

# Example usage
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target = 70
    result = interpolation_search(arr, target)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")
