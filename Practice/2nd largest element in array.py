nums = [55,32,97,-55,45,67,89,88,90,99]

def second_largest(nums):
    n = len(nums)
    largest = float("-inf")
    s_largest = float("-inf")

    for i in range(n):
        largest = max(nums[i], largest)

    for i in range(n):
        if nums[i] != largest and nums[i] > s_largest:
            s_largest = nums[i]

    return s_largest

print(second_largest(nums))
