class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indexes = defaultdict(list)
        for i in range(len(s)):
            if not indexes[s[i]]:
                indexes[s[i]] = [i, i]
            else:
                indexes[s[i]][1] = i
        
        res = []
        start, end = 0, 0
        for i in range(len(s)):
            end = max(end, indexes[s[i]][1])
            if i == end or i == len(s) - 1:
                res.append(end - start + 1)
                end += 1
                start = end

        return res