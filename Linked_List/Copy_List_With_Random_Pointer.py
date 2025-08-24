"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        '''Initializes objects needed across the Solution class'''
        # Creates our hash map
        self.map = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''Creates a deep copy of the given list'''
        # Returns a None if the current node is None
        if head is None:
            return None
        # Returns the node in the hashmap if we have already seen this node before
        if head in self.map:
            return self.map[head]
        
        # Creates a copy of the current node
        copy = Node(head.val)
        # Adds the copy to the hashmap
        self.map[head] = copy
        # Finds the next pointer recursively
        copy.next = self.copyRandomList(head.next)
        # Finds the random pointer recursively
        copy.random = self.map.get(head.random)
        # Returns the copy node (the head of the copied list)
        return copy