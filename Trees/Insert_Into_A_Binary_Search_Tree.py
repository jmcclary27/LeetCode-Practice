# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def DFS(root):
            if not root:
                return
            
            if val > root.val and not root.right:
                root.right = TreeNode(val)
                return
            
            if val < root.val and not root.left:
                root.left = TreeNode(val)
                return
            
            if val > root.val:
                DFS(root.right)
            
            if val < root.val:
                DFS(root.left)
        
        DFS(root)
        return root