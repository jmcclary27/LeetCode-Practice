class Solution:
    def encode(self, strs: List[str]) -> str:
        # Checks edge case of there being no strings
        if not strs:
            return ""
        # Creates a list to track the lengths of the strings, and then a blank string that we will later add to
        sizes, res = [], ""
        # Adds the lengths to our sizes list
        for s in strs:
            sizes.append(len(s))
        # Adds the sizes, separated by commas, to the string
        for sz in sizes:
            res += str(sz)
            res += ','
        # Separates sizes and the original strings
        res += '#'
        # Adds the original strings
        for s in strs:
            res += s
        # Returns our final encoded string
        return res

    def decode(self, s: str) -> List[str]:
        # Checks edge case of an empty string
        if not s:
            return []
        # Creates an empty list for our sizes, an empty list for our decoded string, and creates a counter
        sizes, res, i = [], [], 0
        # Loops until finding the separator of the words and sizes
        while s[i] != '#':
            # Initial string to keep track of our separate strings
            cur = ""
            # Loops through adding our sizes the the sizes list while updating the counter so we know what index the sizes end
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        # Loops through adding each string by indexing them from their sizes
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        # Returns final list of strings
        return res