class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        pointer = 0
        n = len(spaces)
        for i in range(len(s)):
            if pointer < n and i == spaces[pointer]:
                res += " "
                pointer += 1
            res += s[i]
        return res