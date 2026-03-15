nums = [5, 9, 4]
target = 9

def subsets_sum(nums, target):
    res = []

    def solve(index, total, subset):
        if total == target:
            res.append(subset.copy())
            return

        if total > target:
            return

        if index >= len(nums):
            return

        # include
        subset.append(nums[index])
        solve(index + 1, total + nums[index], subset)

        # backtrack
        e = subset.pop()

        # exclude
        solve(index + 1, total, subset)

    solve(0, 0, [])
    return res


print(subsets_sum(nums, target))