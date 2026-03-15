# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         n = len(t)

#         for i in range(n):
#             if s.count(t[i]) != t.count(t[i]):
#                 return t[i]

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        x = 0

        for i in range(len(s)):
            x = x ^ ord(s[i])

        for i in range(len(t)):
            x = x ^ ord(t[i])

        return chr(x)