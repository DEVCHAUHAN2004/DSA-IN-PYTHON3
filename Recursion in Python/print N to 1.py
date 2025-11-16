# def print_reverse(n):
#     if n == 0:        # base case
#         return
#     print(n)
#     return print_reverse(n - 1)   # tail call (last operation)

# print_reverse(10)



def func(i, n):
    if n == 0:   # base case
        return
    print(n)
    func(i, n - 1)

func(1, 10)