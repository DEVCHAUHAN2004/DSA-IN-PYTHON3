nums = [1,1,1,2,3,4,4,7,9,9,9,10]
def removeduplicates_from_sorted_array(nums):
  n = len(nums)
  if n == 1:
    return 1
  
  i = 0
  j = i+1

  while j < n:
    if nums[i] != nums[j]:
      i += 1
      nums[i],nums[j] = nums[j],nums[i]
    j += 1
  return i + 1

print(removeduplicates_from_sorted_array(nums))
# 7    