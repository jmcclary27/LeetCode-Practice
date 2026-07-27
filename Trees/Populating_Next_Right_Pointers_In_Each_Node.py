"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return

        q = deque([deque([root]), deque([])])
        while q:
            node = q[0].popleft()

            if q[0]:
                node.next = q[0][0]
            else:
                node.next = None

            if node.left:
                q[1].append(node.left)
            if node.right:
                q[1].append(node.right)

            if not q[0]:
                if q[1]:
                    q.popleft()
                    q.append(deque([]))
                else:
                    break
        return root