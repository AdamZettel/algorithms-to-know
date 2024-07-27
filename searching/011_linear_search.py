def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1  # Return -1 if the target is not found

# Example usage with different numbers
arr = [45, 23, 78, 12, 56, 89, 34]
target = 56
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
