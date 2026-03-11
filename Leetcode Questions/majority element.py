# nums =  [2,2,1,1,1,2,2]
# def majority_element(nums):
#   freq = {}

#   n = len(nums)

#   for i in range(n):
#     if nums[i] in freq:
#       freq[nums[i]] += 1
#     else:
#         freq[nums[i]] = 1

#   for key,value in freq.items():
#       if value > n // 2:
#          return key
      
# print(majority_element(nums))

n = int(input("Enter size: "))

nums = list(map(int, input("Enter elements: ").split()))

def majority_element(nums):
    freq = {}
    
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for key, value in freq.items():
        if value > n // 2:
            return key

print(majority_element(nums))
