class Solution:
    def numDecodings(self, s: str) -> int:
        # Creates the previous and result variable
        # Also creates the safety variable which is used in a special case of finding 10 or 20
        safety, prev, res = 0, 1, 1
        # Loops length of s times
        for i in range(len(s)):
            # Checks if the current number is 0
            if s[i] == '0':
                # Checks if the number is 10 or 20 (only possible cases with s[i] = 0)
                if i != 0 and s[i-1] in '12':
                    # Updates numbers to be back one iteration
                    res = prev
                    prev = safety
                    continue
                # If no 10 or 20 is detected, then it is not a real number to decode with the alphabet
                else:
                    return 0
            # Checks if the last two numbers are valid to decode
            if i != 0 and s[i-1] != '0' and int(str(s[i-1]) + str(s[i])) <= 26:
                # Updates numbers to move up one cycle in the fibonacci sequence
                safety = prev
                temp = res
                res += prev
                prev = temp
                continue
            # Moves safety and prev up one in the sequence
            safety = prev
            prev = res
        # Returns the result
        return res