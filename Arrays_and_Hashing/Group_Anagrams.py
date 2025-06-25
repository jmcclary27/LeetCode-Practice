from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Uses a defaultdict to group anagrams based on character counts.
        # Defaults to a list if the key does not exist.
        res = defaultdict(list)
        # Iterates through the list of strings
        for s in strs:
            # Creates a count array for each string, where index 0 corresponds to 'a', 1 to 'b', ..., 25 to 'z'.
            count = [0] * 26
            # Iterates through each character in the string and increments the corresponding index in the count array.
            for c in s:
                # ord(c) - ord('a') gives the index for the character c in the count array by subtracting their ASCII values.
                count[ord(c) - ord('a')] += 1
            # Converts the count array to a tuple to use it as a key in the dictionary.
            res[tuple(count)].append(s)
        # Returns the values of the dictionary as a list of lists, where each list contains anagrams.
        return list(res.values())