def ternary_search(arr, target, left, right):
    if right >= left:
        # Divide the array into three parts
        third = (right - left) // 3
        mid1 = left + third
        mid2 = right - third
        
        # Check if the target is at one of the mid points
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        
        # Determine which part to search in
        if target < arr[mid1]:
            return ternary_search(arr, target, left, mid1 - 1)
        elif target > arr[mid2]:
            return ternary_search(arr, target, mid2 + 1, right)
        else:
            return ternary_search(arr, target, mid1 + 1, mid2 - 1)
    
    return -1

# Wrapper function to simplify usage
def search(arr, target):
    return ternary_search(arr, target, 0, len(arr) - 1)

# Example usage
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 15
    result = search(arr, target)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")

