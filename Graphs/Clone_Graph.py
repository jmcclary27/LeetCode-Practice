"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Hash map to map the old nodes to the new nodes
        oldToNew = {}

        # Recursive DFS function
        def dfs(node):
            # Returns if node has already been seen
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            # Calls dfs on each neighbor
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        # Returns the results from the DFS function
        return dfs(node) if node else None