def convert2binary(nums):
    res = ""
    
    while nums > 0:
        if nums % 2 == 1:
            res += "1"
        else:
            res += "0"
        nums = nums // 2

    res = res[::-1]
    return res


nums = int(input("enter:"))
print(convert2binary(nums))