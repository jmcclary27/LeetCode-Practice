class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        if n < 3:
            return ""
        
        maxx = -1
        for i in range(n - 2):
            curr = num[i : i + 3]
            if curr[0] == curr[1] and curr[0] == curr[2] and int(curr) > int(maxx):
                maxx = curr

        return "" if maxx == -1 else maxx