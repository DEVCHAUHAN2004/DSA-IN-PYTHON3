nums = [5, 9, 1, 2, 4, 15, 6, 3]
target = 13

def two_sum(nums, target):
    n = len(nums)
    for i in range(0,n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # in case no pair found

print(two_sum(nums, target))
# [1, 4]

