def postfix_to_infix(exp):
    stack = []

    for i in range(len(exp)):
        ch = exp[i]

        # if operand
        if ch.isalnum():
            stack.append(ch)

        # if operator
        else:
            op2 = stack.pop()
            op1 = stack.pop()

            temp = "(" + op1 + ch + op2 + ")"
            stack.append(temp)

    return stack[-1]


# Example
exp = "ab-de+f*/"
print(postfix_to_infix(exp))