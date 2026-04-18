class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for ops in logs:
            if ops[:-1] == ".":
                continue
            elif ops[:-1] == "..":
                if res != 0:
                    res -= 1
            else:
                res += 1
        return res