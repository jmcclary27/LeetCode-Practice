# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Checks if the root we are given exists and returns None if not
        if not root: return None

        # Flips the nodes children
        root.left, root.right = root.right, root.left

        # Applies recursive DFS
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Returns the current root
        return root