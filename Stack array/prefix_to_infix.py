def prefix_to_infix(n):
    stack = []

    # traverse right to left 🔥
    for i in range(len(n)-1, -1, -1):
        char = n[i]

        if char.isalnum():
            stack.append(char)
        else:
            op1 = stack.pop()
            op2 = stack.pop()

            new = "(" + op1 + char + op2 + ")"
            stack.append(new)

    return stack[-1]


# Example
n = "*+PQ-MN"
x = prefix_to_infix(n)

print(x)