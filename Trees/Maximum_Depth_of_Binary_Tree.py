# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Checks if the root given exists and returns a depth of 0 if not
        if not root: return 0

        # Applies recursive DFS and adds one for each function call
        leftdepth = self.maxDepth(root.left) + 1
        rightdepth = self.maxDepth(root.right) + 1

        # Returns the max depth between the left and right side
        return max(leftdepth, rightdepth)