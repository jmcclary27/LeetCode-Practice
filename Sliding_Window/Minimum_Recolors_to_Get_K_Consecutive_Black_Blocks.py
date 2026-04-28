class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, k - 1
        curr = 0

        for i in range(k):
            if blocks[i] == 'W':
                curr += 1
        res = curr

        while r < len(blocks) - 1:
            if blocks[l] == 'W' and blocks[r+1] == 'B':
                curr -= 1
            elif blocks[l] == 'B' and blocks[r+1] == 'W':
                curr += 1
            l += 1
            r += 1
            res = min(curr, res)
        return res