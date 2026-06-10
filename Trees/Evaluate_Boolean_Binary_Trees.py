# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return
        
        if root.left:
            left = self.evaluateTree(root.left)
            right = self.evaluateTree(root.right)

            if root.val == 2:
                return left or right
            else:
                return left and right
        else:
            if root.val == 0:
                return False
            else:
                return True