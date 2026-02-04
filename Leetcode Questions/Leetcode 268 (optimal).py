nums = [9,6,4,2,3,5,7,0,1]

def missing_number(nums):
  n = len(nums)
  expected_sum = n*(n+1) // 2
  actual_sum = sum(nums)

  x = expected_sum - actual_sum
  return x

print(missing_number(nums))
