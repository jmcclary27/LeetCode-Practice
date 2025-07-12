# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Establishes two nodes to keep track of the current and previous node
        prev, curr = None, head
        # Loops until we reach the end of the linked list (curr is None)
        while curr:
            # Creates a temporary variable so we can change curr.next without having a memory leak
            temp = curr.next
            # Points the next node to be behind us
            curr.next = prev
            # Shifts the prev node up one
            prev = curr
            # Shifts the curr node up one
            curr = temp
        # Returns the tail of the sorted list (head of reversed list)
        return prev