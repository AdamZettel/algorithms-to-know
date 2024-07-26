def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Find the maximum value to determine the range of buckets
    max_val = max(arr)
    
    # Create buckets and initialize them
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
    
    # Determine the range of each bucket and distribute the elements
    for num in arr:
        index = num * bucket_count // (max_val + 1)
        buckets[index].append(num)
    
    # Sort each bucket and concatenate the results
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    return sorted_arr

# Example usage with different numbers
arr = [45, 23, 78, 12, 56, 89, 34]
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)
