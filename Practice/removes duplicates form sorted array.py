nums = [1,1,1,2,3,4,4,7,9,9,9,10]

def removeduplicates_from_sorted_array(nums):
    n = len(nums)
    freq_map = {}   # dictionary

    # keys store karne ke liye (tumhari hi line)
    for i in range(n):
        freq_map[nums[i]] = 0   # value use nahi karni, sirf keys chahiye

    j = 0
    # dictionary ke keys insertion order ke hisaab se uthenge (sorted array ke liye safe)
    for key in freq_map:
        nums[j] = key
        j += 1

    return j

print(removeduplicates_from_sorted_array(nums))
# 7


# nums = [1,1,1,2,3,4,4,7,9,9,9,10]

# def removeduplicates_from_sorted_array(nums):
#     n = len(nums)
#     freq_map = {}

#     for i in range(n):
#         freq_map[nums[i]] = 0   # store unique keys only

#     j = 0
#     for key in freq_map:
#         nums[j] = key
#         j += 1

#     return j

# k = removeduplicates_from_sorted_array(nums)
# print("Total unique elements:", k)
# print("Array after removing duplicates:", nums[:k])

# Total unique elements: 7
# Array after removing duplicates: [1, 2, 3, 4, 7, 9, 10]
