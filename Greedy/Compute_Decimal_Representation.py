class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        res = []
        num = str(n)
        length = len(num)
        for i in range(length):
            if num[i] != "0":
                res.append(int(num[i]) * (10 ** (length - i - 1)))
        return res