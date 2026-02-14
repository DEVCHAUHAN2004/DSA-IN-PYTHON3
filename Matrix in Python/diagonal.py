nums = [[5,2,3],[1,4,6],[7,4,9]]

def diagonal(nums):
    rows = len(nums)
    columns = len(nums[0])

    for i in range(rows):
        for j in range(columns):
            if i == j:
                print(nums[i][j],end= ' ')
            else:
                print("*", end=' ')
        print()   # new line after each row

diagonal(nums)

# 5 * * 
# * 4 * 
# * * 9

nums = [[5,2,3],[1,4,6],[7,4,9]]

def diagonal_sum(nums):
    rows = len(nums)
    d_sum = 0   # bahar rakho

    for i in range(rows):
        for j in range(len(nums[0])):
            if i == j:
                d_sum += nums[i][j]
                print(nums[i][j], end=' ')
            else:
                print("*", end=' ')
        print()   # new line after each row

    print("Diagonal sum =", d_sum)

diagonal_sum(nums)
# 18


# 5 * * 
# * 4 * 
# * * 9