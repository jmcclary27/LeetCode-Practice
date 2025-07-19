# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initializes the two pointers
        slow, fast = head, head

        # Checks if our fast pointer is on None or will reach None within this iteration
        # Since we increment fast by two for each iteration, our loop condition checks both fast and fast.next
        while fast and fast.next:
            # Increments our slow pointer by one
            slow = slow.next
            # Increments our fast pointer by two
            fast = fast.next.next
            # Checks if slow and fast our equal
            if slow == fast:
                # Returns True if a cycle is detected
                return True
        # Returns False if no cycle is detected
        return False