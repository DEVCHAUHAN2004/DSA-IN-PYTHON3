nums = [5,9,4]

def subsets_ka_sum(nums):
  res = []

  def solve(index, nums, subset, res):
    if index >= len(nums):
      res.append(sum(subset))
      return
    
    subset.append(nums[index])
    solve(index+1, nums, subset, res)

    subset.pop()

    solve(index+1, nums, subset, res)

  solve(0, nums, [], res)
  return sorted(res)

# 👉 print यहाँ लगाओ
print(subsets_ka_sum(nums))