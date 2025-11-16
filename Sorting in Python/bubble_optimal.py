nums = [5,1,6,8,2,4,9]

def bubble_sort(nums):
    n = len(nums)
    
    for i in range(n-2,-1,-1):
        is_swap = False   # har pass ke start me FALSE
        
        for j in range(0,i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_swap = True    # swap hua → TRUE
                
        if is_swap == False:   # agar ek bhi swap nahi hua
            break         # array already sorted → break
    
    return nums

print(bubble_sort(nums))
# [1, 2, 4, 5, 6, 8, 9]
