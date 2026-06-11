class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}
        curr, res = 0, 0

        for r in range(len(s)):
            if r < k:
                if s[r] in vowels:
                    curr += 1
                    res = curr
                continue
            if s[r - k] in vowels:
                curr -= 1
            if s[r] in vowels:
                curr += 1
            res = max(res, curr)
        
        return res