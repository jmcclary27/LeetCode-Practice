# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def add(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        '''Recursive helper function that tracks the current node
           of the two lists as well as the carry from adding numbers
           with a sum greater than ten.'''
        # Base case for reaching the end of the list
        if not l1 and not l2 and carry == 0:
            return None

        # Stores the current nodes' values
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        # Calculates carry if any
        carry, val = divmod(v1 + v2 + carry, 10)

        # Recursively finds the next node
        next_node = self.add(
            l1.next if l1 else None,
            l2.next if l2 else None,
            carry
        )
        # returns the head of the list
        return ListNode(val, next_node)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Calls helper function and returns result
        return self.add(l1, l2, 0)