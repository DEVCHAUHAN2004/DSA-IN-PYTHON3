# 2404. Most Frequent Even Element
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, return the most frequent even element.

# If there is a tie, return the smallest one. If there is no such element, return -1.

 

# Example 1:

# Input: nums = [0,1,2,2,4,4,1]
# Output: 2
# Explanation:
# The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
# We return the smallest one, which is 2.
# Example 2:

# Input: nums = [4,4,4,9,2,4]
# Output: 4
# Explanation: 4 is the even element appears the most.
# Example 3:

# Input: nums = [29,47,21,41,13,37,25,7]
# Output: -1
# Explanation: There is no even element.

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums)

        # upar range wala loop
        for i in range(n):
            if nums[i] % 2 == 0:
                if nums[i] in freq:
                    freq[nums[i]] += 1
                else:
                    freq[nums[i]] = 1

        if not freq:
            return -1

        max_freq = max(freq.values())

        res = []

        # yaha items wala loop
        for key, value in freq.items():
            if value == max_freq:
                res.append(key)

        return min(res)