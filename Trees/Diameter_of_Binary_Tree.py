# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Creates the result variable
        res = 0

        # Creates a nested function to apply recursive DFS
        def dfs(root):
            # Declares the result variable within the function
            nonlocal res

            # Checks if the root exists and returns a diameter of 0 if it doesn't
            if not root:
                return 0
            # Applies recursive DFS
            left = dfs(root.left)
            right = dfs(root.right)
            # Assigns res the max of the current result and the addition of the left and right side depth (diameter)
            res = max(res, left + right)

            # Returns 1 plus the longest depth
            return 1 + max(left, right)

        # Executes the dfs function
        dfs(root)
        # Returns the result
        return res