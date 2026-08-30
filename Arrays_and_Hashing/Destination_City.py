class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        seen = defaultdict(list)
        for a, b in paths:
            seen[a].append(b)
        for a, b in paths:
            if a not in seen:
                return a
            if b not in seen:
                return b