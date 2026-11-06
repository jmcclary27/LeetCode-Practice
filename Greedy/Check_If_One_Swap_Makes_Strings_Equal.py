class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        different = [i for i in range(len(s1)) if s1[i] != s2[i]]
        if not different: return True
        if len(different) != 2: return False
        a,b = different
        return s1[a] == s2[b] and s1[b] == s2[a]
