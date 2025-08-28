class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        # Recursive DFS function
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Decision to not include nums[i]
            subset.pop()
            dfs(i + 1)

        # Calls DFS starting at index 0
        dfs(0)
        return res