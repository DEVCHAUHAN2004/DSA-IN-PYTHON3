# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num-1 in nums:
                continue
            count = 1
            while num + count  in nums:
                count += 1
            res = max(res, count)
        return res
        # my_set = set()
        # n = len(nums)

        # for i in range(n):
        #     my_set.add(nums[i])

        # longest = 0
        # for num in my_set:
        #     if num - 1 not in my_set:
        #         x = num          
        #         count = 1

        #         while x + 1 in my_set:
        #             count += 1
        #             x += 1

        #         longest = max(longest, count)

        # return longest
