def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swaps were made in this pass
        swapped = False
        # Iterate through the array up to the last unsorted element
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps were made, the array is already sorted
        if not swapped:
            break
    return arr

# Example usage
arr = [32, 34, 2, 11, 7, 11, 10]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
