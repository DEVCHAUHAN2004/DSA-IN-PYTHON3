nums = [9,6,4,2,3,5,7,0,1]

def missing_number(nums):
  n = len(nums)
  # for i in range(0,n+1):
  #   if i not in nums:
  #     return i
  freq_map = {}
  for i in range(0,n+1):
    freq_map[i] = 0

  for num in nums:
    freq_map[num] = 1

  for key, value in freq_map.items():
    if value == 0:
      return key     
    # 8



print(missing_number(nums))
    # 2

    