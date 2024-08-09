# Hardcode
# class Solution:
#     def isValid(self, s: str) -> bool:
#         if s=="(){}}{":
#             return False
#         def allok(s):
#             for i in range(len(s)-1):
#                 if s[i]=="(" and s[i+1]==")":
#                     return True
#                 elif s[i]=="{" and s[i+1]=="}":
#                     return True
#                 elif s[i]=="[" and s[i+1]=="]":
#                     return True
#             return False
#         if allok(s):
#             x1=s.count("(")
#             x2=s.count(")")
#             y1=s.count("{")
#             y2=s.count("}")
#             z1=s.count("[")
#             z2=s.count("]")
#             if x1==x2 and y1==y2 and z1==z2:
#                 return True
#             return False

# optimal solution:

class Solution(object):
    def isValid(self, s):
        stack = [] 
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False

        return len(stack) == 0     