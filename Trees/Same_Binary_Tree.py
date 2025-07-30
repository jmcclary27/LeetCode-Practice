# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Returns True if both nodes are None (We have reached the end of the tree for both trees)
        if not p and not q:
            return True
        # Checks if p and q are the exact same and executes recursive DFS if so
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # Returns False if they are not the exact same
        else:
            return False