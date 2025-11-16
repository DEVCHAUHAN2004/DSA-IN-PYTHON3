n = int(input("Enter the number: "))

num = n
total = 0
x = len(str(n))

while num > 0:
    digit = num % 10
    total = total + (digit ** x)
    num = num // 10

if total == n:
    print(n, "is an Armstrong Number ✅")
else:
    print(n, "is NOT an Armstrong Number ❌")

# Enter the number: 153
# 153 is an Armstrong Number ✅

# Enter the number: 45465
# 45465 is NOT an Armstrong Number ❌