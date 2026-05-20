class Solution:
    def makeGood(self, s: str) -> str:
        i = 1
        s = list(s)
        while i < len(s):
            if (s[i].islower() and s[i - 1].isupper() or s[i].isupper() and s[i - 1].islower()) and s[i].lower() == s[i - 1].lower():
                s.pop(i)
                s.pop(i - 1)
                i = 1
            else:
                i += 1
        return "".join(s)