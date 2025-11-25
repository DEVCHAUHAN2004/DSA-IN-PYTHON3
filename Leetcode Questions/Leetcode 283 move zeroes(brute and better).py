nums = [1,0,2,4,3,0,0,6,5,1]

def move_zeroes(nums):
  n = len(nums)
  res = []
  for i in range(0,n):
    if nums[i] != 0:
      res.append(nums[i])

  m = len(res)
  for i in range(0,m):
    nums[i] = res[i]

  for i in range(m,n):
    nums[i] = 0
  return nums

print(move_zeroes(nums))
# [1, 2, 4, 3, 6, 5, 1, 0, 0, 0]

