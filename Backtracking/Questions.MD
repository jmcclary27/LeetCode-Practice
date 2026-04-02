# Descriptions and any additional notes for every questions written below

## Sum of All Subsets XOR Total (Easy)

The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.
For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
You are given an array nums, return the sum of all XOR totals for every subset of nums.
Note: Subsets with the same elements should be counted multiple times.
An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

## Subsets (Medium)

Given an array nums of unique integers, return all possible subsets of nums.
The solution set must not contain duplicate subsets. You may return the solution in any order.

Idea: The idea here is to have create a global array that stores all the subsets, and we find these subsets by using DFS. In our DFS function, we either decide to add the current number, or we don't. We do this by appending the current number to the subset and running dfs, then popping that number and running it again. Since we are running all 2^n possibilities for subsets, and the subsets can be up to length n, this answer has a O(n*2^n) time complexity with the same space complexity.

## Combination Sum (Medium)

You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.
The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.
You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Idea: This solution is similar to the last one, except our two split decisions are to stay on the same number and increment the total, or to move up a number and not increment the total. This code runs in (2^t/m) times and has a space complexity of (t/m).

## Combination Sum (Medium)

You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.
Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.
You may return the combinations in any order and the order of the numbers in each combination can be in any order.

## Combination (Medium)

You are given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

## Permutations (Medium)

Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.