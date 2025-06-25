class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Creates a dictionary to store previously seen numbers and their indices.
        prevMap = {}

        # Iterates through the list of numbers with i being the index and n being the number.
        for i, n in enumerate(nums):
            # Calculates the difference needed to reach the target.
            diff = target - n
            # Checks if the difference is already in the map.
            if diff in prevMap:
                # If found, returns the indices of the two numbers that add up to the target.
                # Since prevMap[diff] will always be found before n, it ensures the first index is less than the second.
                return [prevMap[diff], i]
            # If not found, adds the current number and its index to the map.
            prevMap[n] = i