class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        seen = {}
        for key, val in knowledge:
            seen[key] = val

        res = ""
        i = 0
        while i < len(s):
            if s[i] == ")":
                continue
            elif s[i] == "(":
                string = ""
                i += 1
                while i < len(s) and s[i] != ")":
                    string += s[i]
                    i += 1
                print(string)
                if string in seen:
                    res += seen[string]
                else:
                    res += "?"
            else:
                res += s[i]
            i += 1
        return res