def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Choose a pivot element
        pivot = arr[len(arr) // 2]
        # Partitioning step
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        # Recursively apply quick_sort to the partitions
        return quick_sort(left) + middle + quick_sort(right)

# Example usage with different numbers
arr = [45, 23, 78, 12, 56, 89, 34]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
