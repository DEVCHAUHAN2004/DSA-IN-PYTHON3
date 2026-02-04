nums = [5, 9, 1, 2, 4, 15, 6, 3]
target = 19

def two_sum(nums, target):
    n = len(nums)
    freq = {}

    for i in range(n):
        remaining = target - nums[i]
        if remaining in freq:
            return [freq[remaining], i]
        else:
            freq[nums[i]] = i

print(two_sum(nums, target))
# [4, 5]