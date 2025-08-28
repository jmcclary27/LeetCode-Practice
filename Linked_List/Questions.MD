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

## Reorder Linked List (Medium)

You are given the head of a singly linked-list.
The positions of a linked list of length = 7 for example, can intially be represented as:
[0, 1, 2, 3, 4, 5, 6]
Reorder the nodes of the linked list to be in the following order:
[0, 6, 1, 5, 2, 4, 3]
Notice that in the general case for a list of length = n the nodes are reordered to be in the following order: 
[0, n-1, 1, n-2, 2, n-3, ...]
You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Idea: The idea here is to reverse the second half of the list, so we can then move through the first and second half, connecting them one by one. We first find the halfway point using fast and slow pointers. We then loop from the slow pointer to the end, reversing that half of the linked list. We then connect the first half to the second half by alternating back and forth. This strategy is O(n) runtime and O(1) space.

## Remove Nth Node From End of List (Medium)

You are given the beginning of a linked list head, and an integer n.
Remove the nth node from the end of the list and return the beginning of the list.

Idea: The idea here is to create two pointers, one at the head of the list, and one pointing to the head of the list (one behind the first one). We then increment the one at the head n times, so that it is n + 1 spaces ahead of the left one. We then increment both pointers until the right one is at a None value. When right is at None, the left pointer should be one behind our target pointer, which is the pointer n spaces from the back. We then make the left pointers next point to next next, effectively removing the node. We then return the head of the list for a O(n) runtime complexity and a O(1) space complexity.

## Copy List With Random Pointer (Medium)

You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.
Create a deep copy of the list.
The deep copy should consist of exactly n new nodes, each including:
The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node
Note: None of the pointers in the new list should point to nodes in the original list.
Return the head of the copied linked list.
In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

Idea: The idea here is to create a hash map in the initializer of the class since we will be recursively navigating through the linked list. We navigate using recursion so when we are done we can easily return the head of the list, and while we are finding the next pointers using recursion, our hash map will copy each node so when we return we will know what that nodes random pointer is too. So we set up the base cases of head being None and head being in the hashmap, and other than that we just add head to the map with its copied node as the value, then we call the function using head.next, and after the recursive call we get head.random from the map, because by the time that is called, the map will already have every node in it. This function runs in O(n) runtime and space complexity.

## Add Two Numbers (Medium)

You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.
The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.
Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Return the sum of the two numbers as a linked list.

Idea: The idea is to create a recursive helper function that not only keeps track of the current node for each list, but the carry from addition as well. This method O(m + n) for both the time and space complexity.

## Merge K Sorted Lists (Hard)

You are given an array of k linked lists lists, where each list is sorted in ascending order.
Return the sorted linked list that is the result of merging all of the individual linked lists.

Idea: The idea is to create a previous and current node pointer for lists to create the new list. I made an outer while loop that loops until all the lists have been iterated through, and then an inner for loop that checks each head of the list and finds the smallest value between them. When the smallest value is found, we set previous.next to point to it, and then shift the previous and current node up one. Lastly, we remove that node from the original list.