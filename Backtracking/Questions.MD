# Descriptions and any additional notes for every questions written below

## Subsets (Medium)

Given an array nums of unique integers, return all possible subsets of nums.
The solution set must not contain duplicate subsets. You may return the solution in any order.

Idea: The idea here is to have create a global array that stores all the subsets, and we find these subsets by using DFS. In our DFS function, we either decide to add the current number, or we don't. We do this by appending the current number to the subset and running dfs, then popping that number and running it again. Since we are running all 2^n possibilities for subsets, and the subsets can be up to length n, this answer has a O(n*2^n) time complexity with the same space complexity.

## Combination Sum (Medium)

You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.
The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.
You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Idea: This solution is similar to the last one, except our two split decisions are to stay on the same number and increment the total, or to move up a number and not increment the total. This code runs in (2^t/m) times and has a space complexity of (t/m).