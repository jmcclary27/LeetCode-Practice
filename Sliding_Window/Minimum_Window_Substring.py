class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tSet = Counter(t)
        res, reslen = "", float('inf')

        for i in range(len(s)):
            currSet = Counter()

            for j in range(i, len(s)):
                if s[j] in t and currSet[s[j]] < tSet[s[j]]: currSet[s[j]] += 1

                if currSet == tSet and (j - i + 1) < reslen:
                    reslen = j - i + 1
                    res = s[i:j+1]
                    break
        
        return res