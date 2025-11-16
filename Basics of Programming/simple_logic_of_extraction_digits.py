n = int(input("Enter the number: "))

num = n
while num > 0:
    digit = num % 10      # extract last digit
    print(digit)          # print the digit
    num = num // 10       # remove the last digit
