class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Creates two pointers, indexed at the beginning and end of the string
        l, r = 0, len(s) - 1

        # Loops until the two indexes meet
        while l < r:
            # Skips past non alphanumeric characters for l and r
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            # Returns False if the characters at the two indexes are not equal (Case-insensitive)
            if s[l].lower() != s[r].lower():
                return False
            # Increments and decrements l and r
            l, r = l + 1, r - 1
        # Returns True if False was never returned within the outer while loop
        return True
    
    def alphaNum(self, c):
        '''Returns a boolean representing whether the character passed is within the alphanumeric guidelines specified'''
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))