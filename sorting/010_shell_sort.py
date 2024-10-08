def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        # Perform a gapped insertion sort
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        
        # Reduce the gap
        gap //= 2

    return arr

# Example usage with different numbers
arr = [45, 23, 78, 12, 56, 89, 34]
sorted_arr = shell_sort(arr)
print("Sorted array:", sorted_arr)
