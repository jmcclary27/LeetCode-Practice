class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Creates a set for each character seen
        charSet = set()
        # Creates our left pointer
        l = 0
        # Creates our result variable
        res = 0

        # Loops r through every index
        for r in range(len(s)):
            # Loops until the letter at r is not in the set
            while s[r] in charSet:
                # Removes the letter at l from the charSet
                charSet.remove(s[l])
                # Increments l
                l += 1
            # Adds the letter at r to the set
            charSet.add(s[r])
            # Makes result equal to the max of the current result and the length of the most recent substring
            res = max(res, r - l + 1)
        # Returns the result
        return res