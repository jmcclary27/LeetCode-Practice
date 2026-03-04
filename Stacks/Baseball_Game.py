class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for ops in operations:
            if ops == "+":
                new = stack[-1] + stack[-2]
                stack.append(new)
                res += new
            elif ops == "C":
                new = stack[-1]
                stack.pop()
                res -= new
            elif ops == "D":
                new = stack[-1] * 2
                stack.append(new)
                res += new
            else:
                stack.append(int(ops))
                res += int(ops)
        return res