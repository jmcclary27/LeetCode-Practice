# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Creates a node pointing to the head of the list
        dummy = ListNode(0, head)
        # Creates our left node which is a copy of the dummy node
        left = dummy
        # Creates our right node which is a copy of the head of the list
        right = head

        # Loops until right is n + 1 spaces ahead of left
        while n > 0:
            right = right.next
            n -= 1

        # Loops until right is none, which means left should be one behind the node we are removing
        while right:
            left = left.next
            right = right.next

        # Changes left's pointer to point to the node after the one we are trying to remove
        left.next = left.next.next
        # Returns dummy.next, which is the head of the list
        return dummy.next