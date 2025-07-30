# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Checks if we are given a valid root and returns none if not
        if not root: return None
        # Creates the variable to keep track of the current node we are on
        curr = root
        # Loops until curr is None (There would be no answer in this case)
        while curr:
            # Checks if curr is greater than both and shifts our node to the left (Only works on BSTs)
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
            # Checks if curr is less than both and shifts our node to the right (Only works on BSTs)
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
            # Returns curr if neither case is true (We are on the lower common ancestor)
            else:
                return curr