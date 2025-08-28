class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize pointers and the smallest variable
        L, R = 0, len(nums) - 1
        smallest = min(nums[L], nums[R])
        # Loops until L and R meet
        while L < R:
            # Calculates the middle point
            mid = L + ((R - L) // 2)
            # Checks to find what has the lowest value between the points L, R, and mid
            if nums[L] > nums[R]:
                if nums[mid] > nums[L]:
                    L = mid
                    smallest = nums[R]
                else:
                    smallest = min(nums[R], nums[mid])
                    R = mid
            else:
                return smallest
        return smallest