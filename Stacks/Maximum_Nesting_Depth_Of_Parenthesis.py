class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        res = 0
        for char in s:
            if char == "(":
                stack.append(char)
                res = max(res, len(stack))
            elif char == ")":
                stack.pop()
        return res