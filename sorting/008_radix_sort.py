def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of each digit
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Change count[i] so that count[i] contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr[] contains sorted numbers according to the current digit
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to determine the number of digits
    max_val = max(arr)

    # Apply counting sort to sort elements based on place value.
    exp = 1
    while max_val // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10

    return arr

# Example usage with different numbers
arr = [45, 23, 78, 12, 56, 89, 34]
sorted_arr = radix_sort(arr)
print("Sorted array:", sorted_arr)
