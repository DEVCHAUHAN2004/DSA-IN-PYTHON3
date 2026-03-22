nums = [5, 9, 4]

def subsets_ka_sum(nums):
    result = []

    def solve(ind, total):
        if ind >= len(nums):
            result.append(total)
            return
        
        # include
        solve(ind + 1, total + nums[ind])

        # exclude
        solve(ind + 1, total)

    solve(0, 0)
    return sorted(result)


print(subsets_ka_sum(nums))