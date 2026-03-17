nums = [5, 9, 4]
target = 9

def subsets_sum(nums, target):
    result = []

    def solve(index, subset):
        if index >= len(nums):
            if sum(subset) == target:
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

print(subsets_sum(nums, target))