nums = [5,10,-3,-1,-10,6,10,1-20,-3,-4,10,2]

def rearrange_elements_by_sign(nums):
  n = len(nums)
  pos = []
  neg = []

  for i in range(0,n):
    if nums[i] > 0:
      pos.append(nums[i])
    else:
      neg.append(nums[i])

  for i in range(0,len(pos)):
    nums[2*i] = pos[i]
    nums[2*i+1] = neg[i]
  return nums

print(rearrange_elements_by_sign(nums))
        # [5, -3, 10, -1, 6, -10]