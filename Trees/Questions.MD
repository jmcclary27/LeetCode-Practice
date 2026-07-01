# Descriptions and any additional notes for every questions written below

## Invert Binary Tree (Easy)

You are given the root of a binary tree root. Invert the binary tree and return its root.

Idea: The idea here is to swap the left node with the right node, and then implement recursive DFS by calling the function with root being the left child, and then do it again with the right child. As a base case, if root is None then return None, otherwise return root. This idea runs in O(n) time complexity with O(n) space complexity for the recursion stack because we return something after each function call.

## Maximum Depth of Binary Tree (Easy)

Given the root of a binary tree, return its depth.
The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

Idea: The idea here is to use recursive DFS and to keep track of the depth with each recursive call. We created two variables, leftDepth and rightDepth, and set them equal to 1 + the function calls for the left child and right child. For our base cases, if root is None return 0, otherwise return the max of leftDepth and rightDepth. This runs in O(n) runtime complexity, since it visits each node once, and it has a space complexity of O(height), which is O(logn) in the best case of a balanced tree, and O(n) in the worst case, which is essentially a linked list.

## N-ary Tree Postorder Traversal (Easy)

You are given the root of an n-ary tree, return the postorder traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

## Leaf Similar Trees (Easy)

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

## Path Sum (Easy)

You are given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

## Merge Two Binary Trees (Easy)

You are given two binary trees root1 and root2.
Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.
Return the merged tree.
Note: The merging process must start from the root nodes of both trees.

## Convert Sorted Array To Binary Search Tree (Easy)

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

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

## Binary Tree Inorder Traversal (Easy)

You are given the root of a binary tree, return the inorder traversal of its nodes' values.

## Evaluate Boolean Binary Tree (Easy)

You are given the root of a full binary tree with the following properties:
Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
The evaluation of a node is as follows:
If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
Return the boolean result of evaluating the root node.
A full binary tree is a binary tree where each node has either 0 or 2 children.
A leaf node is a node that has zero children.

## Minimum Distance Between BST Nodes (Easy)

Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

## Count Prefix and Suffix Pairs 1 (Easy)

You are given a 0-indexed string array words.
Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:
isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2, and false otherwise.
For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.
Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.

## Range Sum of BST (Easy)

You are given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

## Binary Tree Preorder Traversal (Easy)

You are given the root of a binary tree, return the preorder traversal of its nodes' values.

## Binary Tree Postorder Traversal (Easy)

You are given the root of a binary tree, return the postorder traversal of its nodes' values.

## Lowest Common Ancestor in Binary Search Tree (Medium)

Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.
The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.

Idea: The idea here is very simple. Since we know our tree is a binary search tree, we check the value of our current node versus the two nodes given. If the value is less then both, we know our two nodes are to the right. If the value is greater than both, we know the two nodes are to the left. If neither or those if statements execute, we know we have reached a split in the tree A.K.A. the lowest common ancestor between the two nodes. This code runs in O(height) for both the runtime and space complexity. 

## Binary Tree Level Order Traversal (Medium)

Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Idea: The idea here is to implement an iterative BFS algorithm, but since we need to keep track of levels, we will use a queue of queues, with the inner queues being separated by their levels. Each time we reach a node, we append its value to our resulting list, and we enqueue its children to the second queue (the last queue) of our outer queue. When the queue we are on is empty, we remove it from the outer queue and add another to both our queue and list. When both the queue we are on and the following queue are empty, we have reached the end of the tree, so we can return our results. This runs in O(n) for both runtime and space complexity.

## Insert Into A Binary Search Tree (Medium)

You are given the root node of a binary search tree (BST) and a value val to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
Note: There may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

## Cousins In A Binary Tree (Medium)

Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.
Two nodes of a binary tree are cousins if they have the same depth with different parents.
Return the root of the modified tree.
Note that the depth of a node is the number of edges in the path from the root node to it.

## Delete Node in a BST (Medium)

You are given a root node reference of a BST and a key, delete the node with the given key in the BST, if present. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.
Note: There can be multiple results after deleting the node, return any one of them.

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

## Construct Binary Tree From Preorder and Inorder Traversal (Medium)

You are given two integer arrays preorder and inorder.
preorder is the preorder traversal of a binary tree
inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.

## Binary Tree Maximum Path Sum (Hard)

Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.
The path sum of a path is the sum of the node's values in the path.