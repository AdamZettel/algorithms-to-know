def counting_sort(arr):
    if len(arr) == 0:
        return arr

    # Find the maximum and minimum values in the array
    max_val = max(arr)
    min_val = min(arr)
    
    # Initialize the count array with zeros
    count_range = max_val - min_val + 1
    count = [0] * count_range
    
    # Count the occurrences of each element
    for num in arr:
        count[num - min_val] += 1
    
    # Build the sorted array
    sorted_arr = []
    for i in range(count_range):
        sorted_arr.extend([i + min_val] * count[i])
    
    return sorted_arr

# Example usage with different numbers
arr = [45, 23, 78, 12, 56, 89, 34]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
