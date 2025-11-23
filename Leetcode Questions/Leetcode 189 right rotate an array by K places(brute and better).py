nums = [3,9,5,6,7,2]
k = 3

def right_rotate_k_places(nums, k):
    n = len(nums)
    rotate = k % n

    for i in range(rotate):
        x = nums.pop()
        nums.insert(0, x)
    return nums    # 🔹 return the rotated list

print(right_rotate_k_places(nums, k))
# [6, 7, 2, 3, 9, 5]




# 🚀 Efficient, 😊 Simple & 🐍 Pythonic Rotation using Slicing (n-k) ✨
# 🔥 Fast, 💡 Clean, 👌 Best for Interviews & LeetCode
# nums = [3,9,5,6,7,2]
# k = 3

# def right_rotate_k_places(nums, k):
#     n = len(nums)
#     k = k % n
#     return nums[n-k:] + nums[:n-k]

# print(right_rotate_k_places(nums, k))
