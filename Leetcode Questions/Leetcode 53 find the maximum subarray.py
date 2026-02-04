nums = [-2,1,-3,4,-1,2,1,-5,4]

def maximum_subarray(nums):
    n = len(nums)
    maxi = float("-inf")

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            maxi = max(maxi, total)
    return maxi

result = maximum_subarray(nums)
print(f"Maximum Subarray Sum = {result}")
# Maximum Subarray Sum = 6