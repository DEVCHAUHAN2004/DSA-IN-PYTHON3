# from typing import List

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         n = len(height)
#         maxwater = 0

#         for i in range(n):
#             for j in range(i + 1, n):
#                 width = j - i
#                 ht = min(height[i], height[j])
#                 area = width * ht

#                 maxwater = max(maxwater, area)

#         return maxwater


# # 👇 VS Code Run Example
# height = [1,8,6,2,5,4,8,3,7]

# obj = Solution()
# print("Max Water =", obj.maxArea(height))

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxwater = 0

        while left < right:
            width = right - left
            ht = min(height[left], height[right])

            area = width * ht
            maxwater = max(maxwater, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxwater