# nums = [5,7,3,2,6,1,5,9,8]
# nums.reverse()
# print(nums)


nums = [5,7,3,2,6,1,5,9,8]

def func(nums, left, right):
    if left >= right:
        return nums

    nums[left], nums[right] = nums[right], nums[left]  # swap
    return func(nums, left + 1, right - 1)  # recursive call

print(func(nums, 0, len(nums) - 1))
# [8, 9, 5, 1, 6, 2, 3, 7, 5]
