class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = None
        minn = float('inf')
        for letter in letters:
            if ord(letter) - ord(target) > 0 and ord(letter) - ord(target) < minn:
                minn = ord(letter) - ord(target)
                res = letter
        return res if res != None else letters[0]