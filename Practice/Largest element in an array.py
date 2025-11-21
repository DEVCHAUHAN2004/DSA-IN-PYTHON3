nums = [55,32,56,78,90,-90,-2,67,89]

def largest_element(nums):
  largest = float("-inf")
  n = len(nums)
  for i in range(n):
    largest = max(largest,nums[i])
  return largest

print(largest_element(nums))
  # 90
  