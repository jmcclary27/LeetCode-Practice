class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = [0] * 26
        for c in chars:
            count[ord(c) - ord('a')] += 1

        org = count[:]
        res = 0

        for w in words:
            good = True
            for c in w:
                i = ord(c) - ord('a')
                count[i] -= 1
                if count[i] < 0:
                    good = False
                    break
            if good:
                res += len(w)

            for i in range(26):
                count[i] = org[i]
        return res