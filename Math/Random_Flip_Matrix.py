from sortedcontainers import SortedSet

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.oneIdxs = SortedSet()

    def flip(self) -> List[int]:
        remainingZeros = self.m * self.n - len(self.oneIdxs)
        zeroIdx = randint(0, remainingZeros - 1)

        idx = zeroIdx
        ones_before_idx = self.oneIdxs.bisect_right(idx) # O(log Flips)
        while idx != zeroIdx + ones_before_idx: # ~O(log Flips) loops
            idx = zeroIdx + ones_before_idx
            ones_before_idx = self.oneIdxs.bisect_right(idx) # O(log Flips)
        
        self.oneIdxs.add(idx)

        return [idx // self.n, idx % self.n]
        
    def reset(self) -> None:
        self.oneIdxs = SortedSet()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()