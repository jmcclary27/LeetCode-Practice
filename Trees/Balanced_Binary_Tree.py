# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Creates our result variable with a default value true
        res = True
        # Applies recursive dfs in a nested function
        def dfs(root):
            # Declares the result within the function
            nonlocal res
            # Checks if the root is None and returns a height and balance of 0 if it is
            if not root:
                return (0, 0)
            
            # Applies recursive DFS
            left = dfs(root.left)
            right = dfs(root.right)

            # Calculates the node's balance
            balance = right[0] - left[0]
            # Returns False if not height balanced
            if balance > 1 or balance < -1:
                res = False

            # Returns the height and the balance
            return (1 + max(left[0], right[0]), balance)
        # Applies the dfs function
        dfs(root)
        # Returns res
        if res:
            return True
        return res