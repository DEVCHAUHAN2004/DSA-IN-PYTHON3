def convert2decimal(str):
    res = 0
    power = 0
    i = len(str) - 1

    while i >= 0:
        if str[i] == '1':
            res = res + (2 ** power)
        power += 1
        i -= 1

    return res


s = input()
print(convert2decimal(s))