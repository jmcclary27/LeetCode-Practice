class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True

        idx, n = 0, len(s)
        for letter in t:
            if letter == s[idx]:
                idx += 1
            if idx == n:
                return True
        return False