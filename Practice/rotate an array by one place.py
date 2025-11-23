nums = [5, -2, 3, 9, 6, 0, 10, 7]

def rotate_array(nums):
    n = len(nums)
    temp = nums[n-1]     # last element store

    # shift elements right
    for i in range(n-2, -1, -1):
        nums[i+1] = nums[i]

    nums[0] = temp       # put last element in front

rotate_array(nums)
print(nums)
 
#     nums[:] = nums[-1:] + nums[:-1]   # ✔ proper slicing

# # [7, 5, -2, 3, 9, 6, 0, 10]