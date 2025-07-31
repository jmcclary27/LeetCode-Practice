# Descriptions and any additional notes for every questions written below

## Subsets (Medium)

Given an array nums of unique integers, return all possible subsets of nums.
The solution set must not contain duplicate subsets. You may return the solution in any order.

Idea: The idea here is to define a nested backtracking function that keeps track of the current starting index and a stack. Within the function, we first add a shallow copy of the stack to res (if not a shallow copy the stack added will always be empty). Then we loop from the starting index to the length of nums. We add the current number to the stack and call backtracking with the new stack and start + 1. We then pop the stack to initiate the backtracking process. At the end, we return result. This solution is O(n*2^n) for both time and space complexity. 