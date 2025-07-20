# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Creates slow and fast pointers to find the middle of the list
        slow, fast = head, head.next
        # Loops until fast is on the last node or None
        while fast and fast.next:
            # Increments slow by one
            slow = slow.next
            # Increments fast by two
            fast = fast.next.next
        
        # Creates a variable which is the start of the second half of the list
        second = slow.next
        # Creates a prev variable with a None value, and sets slow.next to point to it
        prev = slow.next = None

        # Loops until we are at the end of the second half of the list
        # This works because if the list is even, the two halves are equal in length, and if it is odd, the second half is shorter
        while second:
            # Creates a temporary variable so we can still move through the list after breaking connections
            temp = second.next
            # Points the node backwards
            second.next = prev
            # Changes prev to be our current node
            prev = second
            # Makes our current node the next node
            second = temp
        
        # Creates two variabels for our two halves of the list, with the second half starting at the end
        first, second = head, prev
        # Loops until we have looped all the way through the second half
        while second:
            # Creates two temporary variables for the two halves of teh list
            temp1, temp2 = first.next, second.next
            # Points the first half node to the second half node
            first.next = second
            # Points the second half node to the node in front of the first half node
            second.next = temp1
            # Moves first and second up by one
            first, second = temp1, temp2