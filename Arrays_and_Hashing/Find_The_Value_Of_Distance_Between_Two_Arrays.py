class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        counter = 0
        for i in range(len(arr1)):
            num = arr1[i]
            flagged = False
            for j in range(len(arr2)):
                if abs(num - arr2[j]) <= d:
                    flagged = True
                    break
            if not flagged:
                counter += 1
        return counter