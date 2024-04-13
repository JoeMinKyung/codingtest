class Solution(object):
    def isValid(self, s):
        stack = []
        for p in s:
            if p == "(":
                stack.append(")")
            elif p == "[":
                stack.append("]")
            elif p == "{":
                stack.append("}")
            elif not stack or stack.pop() != p:
                return False
        return not stack

sol = Solution()
print(sol.isValid(")("))       # False
print(sol.isValid("([]}"))      # False
print(sol.isValid("{()[]}"))    # True
print(sol.isValid("{(([]))[]}"))# True

# s=")("
# s="([]}"
# s="{()[]}"