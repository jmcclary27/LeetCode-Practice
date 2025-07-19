# Descriptions and any additional notes for every questions written below

## Reverse Linked List (Easy)

Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Idea: The idea is to create two pointers, one keeping track of the current node, and one keeping track of the previous node. We loop until the current node doesn't exist, and within this loop, we create a temporary pointer to keep track of the current node's next pointer. The reason we do this is because we change the current node to point to the previous node, and with that temporary pointer, we still have access to the next node. After we make the current node point to the previous node, we advance them up one. We do this by making the previous node be the current node, and the current node be the next node. This idea takes O(n) time and O(1) space complexity.

## Merge Two Sorted Linked Lists (Easy)

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
The new list should be made up of nodes from list1 and list2.

Idea: The idea here is to create an empty node that keeps track of our progress through the linked lists. If the current value in list1 is less than the current value at list2, we update the node to point to list1, and then we advance list1 by one. If the current value is list1 is not less than the current value at list2, we do the same thing as last time, but with list2. We do this within a while loop that loops until we reach the end of one of the lists, and by this time, our node should have traversed all of one list, so we can just make node point to the rest of the other list. We return our final list for a time complexity of O(n+m) and a space complexity of O(1). It is important to note that the space complexity is O(1) because we are connecting our lists together and editing them in place. Our node we created helps us traverse these two lists, it does NOT create a new list.

## Linked List Cycle Detection (Easy) 

Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.
Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.
Note: index is not given to you as a parameter.

Idea: Initially, I thought to just create a hash set of everything that has been seen, by our pointer, and if we come across a pointer already in seen, then return True, but I felt that there was a way to solve this problem with a constant space complexity. After futher thought, I realized I could use a fast and slow pointer to detect a cycle. Using this solution there are two outcomes: A) The fast pointer reaches null, meaning there is no cycle, or B) the fast and slow pointer meet again, meaning there is a a cycle. This algorithm has been proven to be O(n) for runtime complexity, and it still maintains that O(1) space complexity I talked about earlier