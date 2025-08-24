class Solution:
    def climbStairs(self, n: int) -> int:
        # Creates variables to keep track of the two previous numbers for fibonacci
        back1, back2 = 1, 0
        # Loops from the second step to the end
        for i in range(1, n + 1):
            # Creates a temporary variable that stores our first back variable
            temp = back1
            # Adds back2 to back1
            back1 += back2
            # Sets back2 equal to temp (previously back1)
            back2 = temp
        # Returns the final answer
        return back1