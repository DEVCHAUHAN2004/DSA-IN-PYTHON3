nums = [[5,2,3],[1,4,6],[7,4,9]]

def matrix(nums):
    rows = len(nums)
    columns = len(nums[0])

    for i in range(rows):
        for j in range(columns):
            print(nums[i][j], end=' ')
        print()   # new line after each row

matrix(nums)

# 5 2 3 
# 1 4 6 
# 7 4 9
