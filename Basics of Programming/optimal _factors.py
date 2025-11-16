from math import sqrt

def getDivisors(nums):
    res = []

    for i in range(1, int(sqrt(nums)) + 1):
        if nums % i == 0:
            res.append(i)
            if nums // i != i:  # to avoid duplicates (like 4 * 4 = 16)
                res.append(nums // i)

    res.sort()
    return res

# user input
nums = int(input("Enter the number: "))
print("Divisors of", nums, "are:", getDivisors(nums))
# Enter the number: 96
# Divisors of 96 are: [1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 96]
