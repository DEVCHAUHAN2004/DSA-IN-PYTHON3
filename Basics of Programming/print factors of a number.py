n = int(input("Enter the number: "))

res = []
for i in range(1, n + 1):
    if n % i == 0:
        res.append(i)

print("Divisors of", n, "are:", res)
# Enter the number: 45
# Divisors of 45 are: [1, 3, 5, 9, 15, 45]


# def getDivisors(n):
#     res = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             res.append(i)
#     return res

# # user input
# n = int(input("Enter the number: "))
# print("Divisors of", n, "are:", getDivisors(n))
