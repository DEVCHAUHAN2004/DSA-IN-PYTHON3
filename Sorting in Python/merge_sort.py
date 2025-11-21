nums = [3,1,2,4,1,5,2,6,4,7,8,9,4,6,3,5]

# Function to merge two sorted arrays
def merge_array(left, right):
    i = j = 0                         # pointers for left and right arrays
    n = len(left)
    m = len(right)
    res = []                          # result array

    # Compare both arrays and pick smaller element
    while i < n and j < m:
        if left[i] <= right[j]:
            res.append(left[i])       # take from left
            i += 1
        else:
            res.append(right[j])      # take from right
            j += 1

    # Add remaining elements from left
    while i < n:
        res.append(left[i])
        i += 1

    # Add remaining elements from right
    while j < m:
        res.append(right[j])
        j += 1

    return res


# Main merge sort function
def merge_sort(nums):
    # Base condition: single element is already sorted
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2              # find middle

    # Divide array into two halves
    left_arr  = nums[:mid]
    right_arr = nums[mid:]

    # Recursively sort both halves
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    # Merge both sorted halves
    return merge_array(left, right)


# Run merge sort
print(merge_sort(nums))
# [1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 8, 9]


"""
---------------------------------------------------------------
                   TIME & SPACE COMPLEXITY
---------------------------------------------------------------

Time Complexity:
    - Splitting takes log n levels
    - Merging each level takes O(n)
    => Overall: O(n log n)

Space Complexity:
    - Extra array used during merging: O(n)
    - Recursion stack depth: O(log n)
    => Total: O(n)

---------------------------------------------------------------
"""
