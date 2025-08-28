# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Creates a variable storing the number of linked lists
        numLists = len(lists)
        # Creates a few empty nodes
        dummy = prev = node = ListNode()

        # Loops until we have reached the end of all the lists
        while any(lists):
            # Creates a variable to hold the smallest value
            smallest = float('inf')
            # Loops through the current node of each list
            for i in range(numLists):
                # Checks if the current node exists and if its value is less than the smallest variable
                if lists[i] and lists[i].val < smallest:
                    # Updates smallest as well as the current node to add to the list
                    smallest = lists[i].val
                    node = lists[i]
                    ith = i
            # Shifts the previous and current node up one
            prev.next = node
            prev = prev.next
            # Deletes the current node from the original list
            temp = lists[ith].next
            lists[ith].next = None
            lists[ith] = temp
        
        # Returns the head
        return dummy.next