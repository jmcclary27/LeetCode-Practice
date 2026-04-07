class Solution:
    def mySqrt(self, x: int) -> int:
        diff = float('inf')
        closest = -1

        l, r = 0, x
        while l <= r:
            mid = l + ((r-l)//2)
            mm = mid * mid
            if mm == x:
                return mid
            if mm > x:
                r = mid - 1
            else:
                if abs(mm - x) < diff:
                    diff = abs(mm - x)
                    closest = mid
                l = mid + 1
        return closest