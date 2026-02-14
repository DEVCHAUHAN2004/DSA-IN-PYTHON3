def count_occurrences(nums, target):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    return freq.get(target, 0)


nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]
target = 3

print(count_occurrences(nums, target))
