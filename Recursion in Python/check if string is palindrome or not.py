s = "nitin"

def checkifstring_palindrome_or_not(s):
    n = len(str(s))
    left = 0
    right = n - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True  

print(checkifstring_palindrome_or_not(s))
