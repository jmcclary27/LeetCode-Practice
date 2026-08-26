class Solution:
    from collections import Counter
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        for val in counter.values():
            if val % 2 == 0:
                res += 2
            else:
                res += 1
        return res