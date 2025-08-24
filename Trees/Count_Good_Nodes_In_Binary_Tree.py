# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, greatest):
            ''' Depth first seach algorithm in a nested function '''
            # Creates a counter of the current good nodes
            total = 0
            # If we are on a None value then the current amount of known good nodes from the bottom is 0
            if not root:
                return 0
            # Checks if the current node is a good node
            if root.val >= greatest:
                # Sets our greates variable to equal the current value
                greatest = root.val
                total = 1
            # Recursively finds the total number of good nodes on the left side
            leftTotal = dfs(root.left, greatest)
            # Recursively finds the total number of good nodes on the right side
            rightTotal = dfs(root.right, greatest)
            # Adds the current number of good nodes plus the amount found on the left and right side
            return leftTotal + rightTotal + total
        # Returns the result from the nested function
        return dfs(root, root.val)