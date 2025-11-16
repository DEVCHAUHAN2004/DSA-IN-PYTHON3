def isArmstrong(num: int) -> bool:
    # total digits count
    order = len(str(num))
    
    # sum of each digit raised to 'order'
    total = 0
    temp = num
    
    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp //= 10
    
    # check condition and return True or False
    return num == total


# Example test
n = int(input("Enter a number: "))
if isArmstrong(n):
    print(f"{n} is an Armstrong Number ✅")
else:
    print(f"{n} is NOT an Armstrong Number ❌")
