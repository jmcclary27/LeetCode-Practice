class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        counter = 0
        for char in s:
            if char == "(":
                counter += 1
            elif char == ")":
                res = max(res, counter)
                counter -= 1
        return max(res, counter)