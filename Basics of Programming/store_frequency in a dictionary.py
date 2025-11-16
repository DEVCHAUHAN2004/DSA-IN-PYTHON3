nums = [1,2,3,4,5,6,2,5,8,9,6,1,3,5,4,7,6,9,6]

def store_frequency(nums):
  freq_map = {}
  n = len(nums)
  for i in range(0,n):
    if nums[i] in freq_map:
      freq_map[nums[i]] += 1
    else:
      freq_map[nums[i]] = 1  
  return freq_map    

print(store_frequency(nums))      
# {1: 2, 2: 2, 3: 2, 4: 2, 5: 3, 6: 4, 8: 1, 9: 2, 7: 1}