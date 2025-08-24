# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Checks if root exists and returns and empty list if not
        if root == None: return []
        # Creates our queue of queues
        q = [[root], []]
        # Creates a list of lists for the result
        res = []
        # Loops until the first queue in q is empty
        while q[0]:
            # Retrieves our node (the first element in the first queue)
            node = q[0].pop(0)
            # Checks if the left node exists
            if node.left:
                # Adds it to the last list in q
                q[-1].append(node.left)
            # Checks if the right node exists
            if node.right:
                # Adds it to the last list in q
                q[-1].append(node.right)
            # Checks if the current queue in q is empty so it can be removed and a new one can be added
            # Also checks if the next queue is empty, because if it is, we have reached the end of the tree
            if len(q[0]) == 0:
                res.append(node.val)
                q.pop(0)
                q.append([])
        # Returns the result
        return res