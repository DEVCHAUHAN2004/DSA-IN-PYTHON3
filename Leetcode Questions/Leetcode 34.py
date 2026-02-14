# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lower_bound(nums, target)
        
        # IMPORTANT FIX
        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]
        
        ub = self.upper_bound(nums, target)

        return [lb, ub - 1]


    def lower_bound(self, nums, target):
        n = len(nums)
        low, high = 0, n - 1
        lb = n   # change from -1 to n

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb


    def upper_bound(self, nums, target):
        n = len(nums)
        low, high = 0, n - 1
        ub = n   # change from -1 to n

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub
