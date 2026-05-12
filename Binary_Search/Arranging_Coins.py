class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 3:
            return n if n == 1 else n - 1

        l, r = 1, (n // 2) + 1
        while l < r:
            mid = (l + r) // 2
            if (mid * (mid + 1)) // 2 <= n:
                l = mid + 1
            else:
                r = mid

        return l - 1