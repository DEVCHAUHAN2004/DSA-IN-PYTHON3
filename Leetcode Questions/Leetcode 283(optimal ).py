nums = [1,0,2,4,3,0,0,6,5,1]

def move_zeroes(nums):
    n = len(nums)
    if n <= 1:
        return nums

    i = 0
    # Find first zero (or non-zero number position)
    while i < n and nums[i] != 0:
        i += 1

    j = i + 1
    while j < n:
        if nums[j] != 0:
            # Swap zero at i with non-zero at j
            nums[i], nums[j] = nums[j], nums[i]
            i += 1  # move i to next zero
        j += 1

    return nums

print(move_zeroes(nums))
# [1, 2, 4, 3, 6, 5, 1, 0, 0, 0]