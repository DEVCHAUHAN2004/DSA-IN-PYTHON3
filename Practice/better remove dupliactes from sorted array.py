nums = [1,1,1,2,3,4,4,7,9,9,9,10]

def removeduplicates_from_sorted_array(nums):
    n = len(nums)
    freq_map = {}   # dictionary
    res = []


    # keys store karne ke liye (tumhari hi line)
    for i in range(n):
        freq_map[nums[i]] = 0   # value use nahi karni, sirf keys chahiye

  
    # dictionary ke keys insertion order ke hisaab se uthenge (sorted array ke liye safe)
    for key in freq_map:
        res.append(key)
      

    return len(res)

print(removeduplicates_from_sorted_array(nums))
# 7