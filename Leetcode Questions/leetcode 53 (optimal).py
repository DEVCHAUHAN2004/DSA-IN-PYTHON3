nums = [-2,1,-3,4,-1,2,1,-5,4]

def maximum_subarray(nums):
    n = len(nums)
    maxi = float("-inf")
    total = 0

    for i in range(n):
        total = total + nums[i]   # add current element
        maxi = max(maxi, total)   # update max

        if total < 0:             # reset if sum becomes negative
            total = 0

    return maxi

print(maximum_subarray(nums))
