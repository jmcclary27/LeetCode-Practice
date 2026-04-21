class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        tidx = 0
        for i in range(len(s)):
            if s[i] == t[tidx]:
                tidx += 1
            if tidx == len(t):
                return 0
        return len(t) - tidx