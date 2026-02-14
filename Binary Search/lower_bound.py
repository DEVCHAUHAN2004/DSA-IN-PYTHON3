nums = [1,1,1,2,3,3,5,6,7,7,7,9,12,13]
target = 3

def lower_bound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    lb = n

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1

    return lb

print(lower_bound(nums, target))
