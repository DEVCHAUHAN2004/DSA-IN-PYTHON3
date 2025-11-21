def insertion_sort(nums):
    n = len(nums)

    for i in range(1, n):
        key = nums[i]
        j = i - 1

        # Shift larger elements to the right
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

    return nums


# Driver code
nums = [5, 2, 4, 6, 1, 3]
print("Before sorting:", nums)
print("After sorting:", insertion_sort(nums))
# Before sorting: [5, 2, 4, 6, 1, 3]
# After sorting: [1, 2, 3, 4, 5, 6]

