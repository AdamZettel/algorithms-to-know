def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point
        mid = len(arr) // 2
        # Divide the array into two halves
        L = arr[:mid]
        R = arr[mid:]

        # Recursively sort both halves
        merge_sort(L)
        merge_sort(R)

        # Merge the sorted halves
        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

# Example usage with different numbers
arr = [45, 23, 78, 12, 56, 89, 34]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
