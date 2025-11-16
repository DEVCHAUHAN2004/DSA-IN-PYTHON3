nums = [5,7,8,4,1,3,6,9,2]

def selection_sort(nums):
  n = len(nums)
  for i in range(0,n):
    min_index = i
    for j in range(i+1,n):
      if nums[min_index] > nums[j]:
        min_index = j
    nums[i],nums[min_index] = nums[min_index],nums[i]
  return nums

print(selection_sort(nums))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]