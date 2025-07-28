class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Creates a set with the numbers in nums as the key
        numSet = set(nums)
        # Creates variable to keep track of the longest sequence
        longest = 0

        # Loops through the set number by number
        for num in numSet:
            # Checks if num is the start of a sequence
            if (num - 1) not in numSet:
                # Sets length to one
                length = 1
                # Loops until the end of the sequence is found
                while (num + length) in numSet:
                    # Increments length
                    length += 1
                # Stores the larger number between our current longest sequence and our new sequence
                longest = max(length, longest)
        # Returns the length of the longest sequence
        return longest