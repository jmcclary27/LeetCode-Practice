class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Creates our two pointers which point to the beginning and end of the array
        L, R = 0 , len(heights) - 1
        # Creates a variable to keep track of the 
        biggest = 0
        
        # Loops until the two pointers meet
        while L < R:
            # Calculates the current area by multiplying the width (the distance from L to R) by 
            # the height of the container (the smaller height at points L and R)
            area = (R - L) * (min(heights[L], heights[R]))
            # Checks if our new number is larger than our current largest area
            biggest = max(biggest, area)
            # Increments L if the height at R is larger
            if heights[L] < heights[R]:
                L += 1
            # Decrements R if the height at L is larger
            # Also Decrements R if the height at L and R is equal (edge case)
            else:
                R -= 1
        # Returns the largest area
        return biggest