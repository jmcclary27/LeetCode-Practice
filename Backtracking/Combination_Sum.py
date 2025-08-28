class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Creates final array and array to store each subset
        res, subset = [], []

        # Recursive DFS
        def dfs(i, total):
            # Terminating condition
            if total > target or i >= len(nums):
                return
            # Executes if subset is valid
            if total == target:
                res.append(subset.copy())
                return
            
            # Decision to stay on the same number
            subset.append(nums[i])
            dfs(i, total + nums[i])

            # Decision to move to next number
            subset.pop()
            dfs(i + 1, total)

        # Executes DFS starting from the beginning and returns the final array
        dfs(0, 0)
        return res