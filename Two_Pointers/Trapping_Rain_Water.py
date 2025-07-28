class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case for empty input
        if not height:
            return 0

        # Creates the two pointers at the beggining and end of the array
        l, r = 0, len(height) - 1
        # Creates two variables meant to store the max height that l and r come accross
        leftMax, rightMax = height[l], height[r]
        # Creates the result variable
        res = 0
        # Loops until l and r meet
        while l < r:
            # Checks if the highest point for r is greater than the highest point for l
            if leftMax < rightMax:
                # Increments l
                l += 1
                # Checks if the height at the new l is greater than leftMax
                leftMax = max(leftMax, height[l])
                # Adds the difference between the two (adds nothing if leftMax did change in the previous line)
                res += leftMax - height[l]
            # Executes if the highest point for r is less than the highest point for l
            else:
                # Decrements r
                r -= 1
                # Checks if the height at the new r is greater than rightMax
                rightMax = max(rightMax, height[r])
                # Adds the difference between the two (adds nothing if rightMax did change in the previous line)
                res += rightMax - height[r]
        # Returns the final result
        return res