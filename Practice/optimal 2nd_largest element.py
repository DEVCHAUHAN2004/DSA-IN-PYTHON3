nums = [55,32,97,-55,45,67,89,88,90,99]

def second_largest(nums):
    n = len(nums)
    largest = float("-inf")
    s_largest = float("-inf")

    for i in range(0, n):
        # If current number is greater than largest, update both
        if nums[i] > largest:
            s_largest = largest   # previous largest becomes second largest
            largest = nums[i]     # update largest

        # If current number is between largest and second largest (distinct)
        elif nums[i] > s_largest and nums[i] != largest:
            s_largest = nums[i]   # update second largest

    return s_largest

result = second_largest(nums)
print(f"Second Largest Element in list {nums} is: {result}")
# Second Largest Element in list [55, 32, 97, -55, 45, 67, 89, 88, 90, 99] is: 97