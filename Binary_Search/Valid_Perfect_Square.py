class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0 or num == 1:
            return True
        
        l, r = 1, num // 2
        while l <= r:
            mid = l + (r - l) // 2
            mm = mid * mid

            if mm == num:
                return True
            elif mm > num:
                r = mid - 1
            else:
                l = mid + 1
        return False