nums = [[5,2,3],[1,4,6],[7,4,9]]

def upper_matrix(nums):
    rows = len(nums)
    columns = len(nums[0])

    for i in range(rows):
        for j in range(columns):
            if i >= j:
                print(nums[i][j],end= ' ')
            else:
                print("*", end=' ')
        print()   # new line after each row

upper_matrix(nums)

# 5 * * 
# 1 4 * 
# 7 4 9