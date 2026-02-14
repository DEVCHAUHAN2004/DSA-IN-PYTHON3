nums = [
    [1, 2, 8],
    [4, 6, 5],
    [2, 7, 9]
]

n = len(nums)

for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            print(nums[i][j], end=' ')
        else:
            print("*", end=' ')
    print()
# * * 8 
# * 6 * 
# 2 * *