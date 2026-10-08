class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        valid = []
        countl, countr = 0, 0
        start = 0
        for i in range(len(s)):
            char = s[i]
            if char == "(":
                countl += 1
            else:
                countr += 1
            if countl == countr:
                valid.append(s[start:i+1])
                start = i+1
        
        res = ""
        for string in valid:
            res += string[1:-1]
        return res