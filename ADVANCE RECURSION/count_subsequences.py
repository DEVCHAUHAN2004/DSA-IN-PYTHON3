def countSubsequences(nums, k):

    def backtrack(index, total):

        if index >= len(nums):
            if total == k:
                return 1
            return 0

        # pick
        pick = backtrack(index + 1, total + nums[index])

        # not pick
        not_pick = backtrack(index + 1, total)

        return pick + not_pick

    return backtrack(0, 0)


nums = [1,2,1]
k = 2
print(countSubsequences(nums, k))