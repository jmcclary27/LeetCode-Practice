# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Returns True if we have reached the end of the subRoot
        if not subRoot:
            return True
        # Returns False if we have reached the end of the root without reaching the end of the subRoot
        if not root:
            return False

        # Calls the recursive DFS function that checks if root and subRoot are the exact same
        if self.sameTree(root, subRoot):
            return True
        # Recursively checks the children of root
        return (self.isSubtree(root.left, subRoot) or 
               self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Checks if both are None and returns True if so
        if not root and not subRoot:
            return True
        # Checks that both nodes are the same and recursively calls the same function using DFS
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and 
                   self.sameTree(root.right, subRoot.right))
        # Returns false if nodes are different or one exists and the other doesn't
        return False