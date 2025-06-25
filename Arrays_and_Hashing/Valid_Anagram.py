class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            # If lengths are not equal, they cannot be anagrams.
            return False

        # Initializes two dictionaries to count occurrences of each character.
        countS, countT = {}, {}

        for i in range(len(s)):
            # Count occurrences of each character in both strings.
            # Uses get method to handle characters not yet in the dictionary.
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        # Returns True if both dictionaries are equal, indicating an anagram.
        return countS == countT