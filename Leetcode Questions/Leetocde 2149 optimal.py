from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n  # result array
        pos_index = 0  # positives go at even indexes
        neg_index = 1  # negatives go at odd indexes

        for i in range(n):
            if nums[i] > 0:
                res[pos_index] = nums[i]
                pos_index += 2
            else:
                res[neg_index] = nums[i]
                neg_index += 2

        return res

# Example usage
nums = [3, 1, -2, -5, 2, -4]
solution = Solution()
result = solution.rearrangeArray(nums)
print("Original:", nums)
print("Rearranged:", result)

# Original: [3, 1, -2, -5, 2, -4]
# Rearranged: [3, -2, 1, -5, 2, -4]
