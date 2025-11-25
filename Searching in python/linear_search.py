nums = [5,3,9,8,1,6,4,10,3,5,7,8,9]
target = 4

def linear_search(nums, target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    return -1

result = linear_search(nums, target)

if result != -1:
    print(f"🎯 Target {target} found at index 👉 {result}")
else:
    print(f"❌ Target {target} not found in the list.")


# 🎯 Target 4 found at index 👉 6