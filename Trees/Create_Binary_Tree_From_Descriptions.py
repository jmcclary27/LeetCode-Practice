# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mp = {}
        root = {}

        for parent, child, isleft in descriptions:
            if parent not in mp:
                mp[parent] = TreeNode(parent)
            
            if child not in mp:
                mp[child] = TreeNode(child)
            
            if isleft:
                mp[parent].left = mp[child]
            else:
                mp[parent].right = mp[child]
            
            if root.get(parent, 0) != -1:
                root[parent] = 1
            root[child] = -1

        for node, state in root.items():
            if state == 1:
                rootval = node
        
        return mp[rootval]