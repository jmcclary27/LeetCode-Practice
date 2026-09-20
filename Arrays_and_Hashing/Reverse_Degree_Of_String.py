class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            val = ord('z') - ord(s[i]) + 1
            res += val * (i + 1)
        return res