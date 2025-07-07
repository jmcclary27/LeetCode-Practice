class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Creates two pointers at the beginning and end of the array
        L, R = 0 , len(numbers) - 1
        # Loops until L and R meet
        while L < R:
            # Since the array is sorted, we know moving indexes forward gives us a larger sum and
            # moving them backwards gives us a smaller sum
            # Checks if the sum at L and R is less than target
            if numbers[L] + numbers[R] < target:
                # Increments L
                L += 1
            # Checks if the sum at L and R is greater than target
            elif numbers[L] + numbers[R] > target:
                # Decrements R
                R -= 1
            # Executes if the sum is neither greater or smaller than target, meaning we have found our indexes
            else:
                # Returns list of indexes (1-indexed)
                return [L + 1, R + 1]