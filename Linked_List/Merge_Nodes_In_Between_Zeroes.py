# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        start, cur = head, head.next
        prev = None
        curSum = 0
        while cur:
            curSum += cur.val
            if cur.val == 0:
                start.val = curSum
                start.next = cur
                prev = start
                start = start.next
                curSum = 0
            cur = cur.next
        
        prev.next = None
        return dummy.next