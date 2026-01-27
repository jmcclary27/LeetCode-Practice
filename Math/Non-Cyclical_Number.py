class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        while True:
            num = 0
            for i in range(len(str(n))):
                num += (n % 10) ** 2
                n //= 10
            if num == 1:
                return True
            elif num in seen:
                return False
            else:
                n = num
                seen.append(num)