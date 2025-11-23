# 🚀 Optimal Solution: Uses Reverse Method for In-Place Rotation (O(n) Time, O(1) Space) ✨

nums = [3,9,5,6,7,2,10,9]
k = 5

def right_rotate_k_places(nums, k):
    n = len(nums)

    def reverse(nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left  += 1
            right -= 1

    k = k % n
    reverse(nums, n-k, n-1)
    reverse(nums, 0, n-k-1)
    reverse(nums, 0, n-1)

    return nums

rotated = right_rotate_k_places(nums, k)

print(f"🔄 Right Rotated List by {k} positions ➤ {rotated}")
# 🔄 Right Rotated List by 5 positions ➤ [6, 7, 2, 10, 9, 3, 9, 5]