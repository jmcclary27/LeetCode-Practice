# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Creates two empty nodes, one to keep track of where we are, and another so that we 
        # can return the list at the end without having to loop anymore
        dummy = node = ListNode()

        # Loops until we reach the end of one of the two lists
        while list1 and list2:
            # Checks if the current value at list1 is lesser than the current value at list2
            if list1.val < list2.val:
                # Points the node to our current spot in list1
                node.next = list1
                # Advances the list1 node
                list1 = list1.next
            # Executes if current value at list1 is not lesser than the current value at list2
            else:
                # Points the node to our current spot in list2
                node.next = list2
                # Advances the list2 node
                list2 = list2.next
            # Advances the node by one
            node = node.next

        # Connects the end of whatever list we are at the end of to the rest of the other list
        node.next = list1 or list2

        # Returns the head of the new list (in place)
        return dummy.next