# n = "5678"

# num = n
# x = str(len(n))
# print(x)

n = int(input("Enter a number: "))
num = n
count = 0

while num > 0:
    num = num // 10
    count += 1

print("Number of digits:", count)

# Enter a number: 56894
# Number of digits: 5


# 2nd approach
# n = 5873
from math import * 
def count_digits(num):
    return int(log10(num)+1)
x = count_digits(3456)
print(x)
# 4
