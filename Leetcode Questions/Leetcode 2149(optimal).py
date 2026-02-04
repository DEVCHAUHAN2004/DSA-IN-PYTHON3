nums = [5,10,-3,-1,-10,6]

def rearrange_elements_by_sign(nums):
    n = len(nums)
    pos = 0
    neg = 1
    res = [0] * n

    for i in range(0, n):
        if nums[i] >= 0:   # includes zero
            res[pos] = nums[i]
            pos += 2
        else:
            res[neg] = nums[i]
            neg += 2

    return res   # <-- yahi fix tha

print(rearrange_elements_by_sign(nums))
