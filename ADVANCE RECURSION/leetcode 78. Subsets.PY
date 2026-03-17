# 78. Subsets
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
# from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def solve(index, subset):
            
            if index >= len(nums):
                result.append(subset.copy())
                return

            # include
            subset.append(nums[index])
            solve(index + 1, subset)

            # backtrack
            subset.pop()

            # exclude
            solve(index + 1, subset)

        solve(0, [])
        return result