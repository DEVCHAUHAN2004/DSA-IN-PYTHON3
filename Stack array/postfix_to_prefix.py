def postfix_to_prefix(exp):
    stack = []

    for i in range(len(exp)):
        ch = exp[i]

        if ch.isalnum():
            stack.append(ch)
        else:
            op2 = stack.pop()
            op1 = stack.pop()

            new = ch + op1 + op2
            stack.append(new)

    return stack[-1]


# Example
exp = "AB+C*"
print(postfix_to_prefix(exp))