n = int(input())
i = int(input())

if (n & (1 << i)) != 0:
    print("Bit is set")
else:
    print("Bit is not set")