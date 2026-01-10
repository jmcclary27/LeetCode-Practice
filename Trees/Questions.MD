# Descriptions and any additional notes for every questions written below

## Invert Binary Tree (Easy)

You are given the root of a binary tree root. Invert the binary tree and return its root.

Idea: The idea here is to swap the left node with the right node, and then implement recursive DFS by calling the function with root being the left child, and then do it again with the right child. As a base case, if root is None then return None, otherwise return root. This idea runs in O(n) time complexity with O(n) space complexity for the recursion stack because we return something after each function call.

## Maximum Depth of Binary Tree (Easy)

Given the root of a binary tree, return its depth.
The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

Idea: The idea here is to use recursive DFS and to keep track of the depth with each recursive call. We created two variables, leftDepth and rightDepth, and set them equal to 1 + the function calls for the left child and right child. For our base cases, if root is None return 0, otherwise return the max of leftDepth and rightDepth. This runs in O(n) runtime complexity, since it visits each node once, and it has a space complexity of O(height), which is O(logn) in the best case of a balanced tree, and O(n) in the worst case, which is essentially a linked list.

## Diamter of Binary Tree (Easy)

The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.
The length of a path between two nodes in a binary tree is the number of edges between the nodes.
Given the root of a binary tree root, return the diameter of the tree.

Idea: The idea is to created a nested function to apply recursive DFS to keep track of the depth (same algorithm as the answer to the last problem), but there is a slight twist. Instead of just keeping track of the depths and returning the largest depth, we want to return the maximum of our current max and the sum of the left depth and right depth, because that sum is a diameter. This code runs in O(n) runtime complexity, and it has a space complexity of O(height), which is O(logn) in the best case of a balanced tree, and O(n) in the worst case, which is essentially a linked list.

## Balanced Binary Tree (Easy)

Given a binary tree, return true if it is height-balanced and false otherwise.
A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Idea: The idea is another nested DFS recursive function, but this time we are keeping track of both the depth and the balance factor. The balance factor is calculated by suptracting the right depth from the left depth, and if at any point the balance is outside of [-1, 1] we return False. Otherwise we return the balance, and 1 + the max depth from the left and right side. This runs in O(n) runtime complexity, since it visits each node once, and it has a space complexity of O(height), which is O(logn) in the best case of a balanced tree, and O(n) in the worst case, which is essentially a linked list.

## Same Binary Tree (Easy)

Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

Idea: The idea is to define a recursive DFS function, where if the nodes and their values are equal, we return the logical and of the function with the trees left children and right children. If we reach a point where both are None, we return True, as we are at the bottom of the tree and we still havent found any differences. If the nodes are not None and not equal, we return False. This runs in O(n) runtime complexity, since it visits each node once, and it has a space complexity of O(height), which is O(logn) in the best case of a balanced tree, and O(n) in the worst case, which is essentially a linked list.

## Subtree of Another Tree (Easy)

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Idea: The idea here is to essentiall create our own subtree, and check if these subtrees are equal to the real subtree. We do this by creating a second recursive DFS function that checks if the subtree is equal to the one given, and returns True if it is. Back in the main function, if our helper function returns True, then we just return True, otherwise we check again with recursive DFS (we check with the left and right children of the node). This idea runs in O(n * m) with n being the size of the tree and m being the size of the subtree. And it has a space of O(n + m) on the recursive stack, which is the size of the two trees.

## Lowest Common Ancestor in Binary Search Tree (Medium)

Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.
The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.

Idea: The idea here is very simple. Since we know our tree is a binary search tree, we check the value of our current node versus the two nodes given. If the value is less then both, we know our two nodes are to the right. If the value is greater than both, we know the two nodes are to the left. If neither or those if statements execute, we know we have reached a split in the tree A.K.A. the lowest common ancestor between the two nodes. This code runs in O(height) for both the runtime and space complexity. 

## Binary Tree Level Order Traversal (Medium)

Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Idea: The idea here is to implement an iterative BFS algorithm, but since we need to keep track of levels, we will use a queue of queues, with the inner queues being separated by their levels. Each time we reach a node, we append its value to our resulting list, and we enqueue its children to the second queue (the last queue) of our outer queue. When the queue we are on is empty, we remove it from the outer queue and add another to both our queue and list. When both the queue we are on and the following queue are empty, we have reached the end of the tree, so we can return our results. This runs in O(n) for both runtime and space complexity.

## Binary Tree Right Side View (Medium)

You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

Idea: The idea here is to use breadth first search and treat it like a level order traversal. So in my BFS algorithm, I kept track of the tree levels using a queue and queues, and whenever I reached the end of an inner queue, I would push the value of the last node for each level to my results array. This ran in O(n) runtime and space complexity.

## Count Good Nodes In Binary Tree (Medium)

Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x
Given the root of a binary tree root, return the number of good nodes within the tree.

Idea: The idea is to create a recursive depth first search algorithm that keeps track of the current greatest value seen on that path. If the current value is higher than the greatest value, then we return 1 + the total from the left and right side, if not, then it's just the total from the two sides. This runs in O(n) for both runtime and space complexity.

## Valid Binary Search Tree (Medium)

Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.
A valid binary search tree satisfies the following constraints:
The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.