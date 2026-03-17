# # Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# # The solution set must not contain duplicate subsets. Return the solution in any order.

 

# # Example 1:

# # Input: nums = [1,2,2]
# # Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# # Example 2:

# # Input: nums = [0]
# # Output: [[],[0]]
# # from typing import List

# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         res = []

#         def solve(index, subset):
#             res.append(subset.copy())

#             for i in range(index, len(nums)):
#                 if i > index and nums[i] == nums[i-1]:
#                     continue

#                 subset.append(nums[i])
#                 solve(i + 1, subset)
#                 subset.pop()

#         solve(0, [])
#         return res

def subsetsWithDup(nums):
    nums.sort()
    res = []

    def solve(index, subset):
        res.append(subset[:])

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue

            subset.append(nums[i])
            solve(i + 1, subset)
            subset.pop()

    solve(0, [])
    return res


# input
nums = list(map(int, input("Enter numbers: ").split()))

# function call
ans = subsetsWithDup(nums)

# output
for x in ans:
    print(x)