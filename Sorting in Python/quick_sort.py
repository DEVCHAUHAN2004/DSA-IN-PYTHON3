# Quick Sort Using In-Place Partitioning

def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get pivot index
        pi = partition(arr, low, high)
        
        # Recursively sort elements before partition and after partition
        quick_sort(arr, low, pi - 1)   # Left side of pivot
        quick_sort(arr, pi + 1, high)  # Right side of pivot


def partition(arr, low, high):
    pivot = arr[high]   # Choosing last element as pivot
    i = low - 1         # Pointer for smaller element
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    
    # Place pivot at correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return pivot index


# Driver code
arr = [10, 7, 8, 9, 1, 5, 2, 15, 3]
print("Original array:", arr)

quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
# Original array: [10, 7, 8, 9, 1, 5, 2, 15, 3]
# Sorted array: [1, 2, 3, 5, 7, 8, 9, 10, 15]