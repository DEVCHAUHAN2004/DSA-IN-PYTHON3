# Palindrome Number Check

num = int(input("Enter a number: "))

# number ko reverse karne ke liye
rev = 0
temp = num

while temp > 0:
    digit = temp % 10       # last digit nikalo
    rev = rev * 10 + digit  # reverse me add karo
    temp = temp // 10       # last digit hatao

# check karo original aur reverse same hain kya
if num == rev:
    print(num, "is a Palindrome Number ✅")
else:
    print(num, "is NOT a Palindrome Number ❌")

# Enter a number: 123456
# 123456 is NOT a Palindrome Number ❌


# Enter a number: 121
# 121 is a Palindrome Number ✅