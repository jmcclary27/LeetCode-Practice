# Descriptions and any additional notes for every questions written below

## Maximum Subarray (Medium)

Given an array of integers nums, find the subarray with the largest sum and return the sum.
A subarray is a contiguous non-empty sequence of elements within an array.

## Jump Game (Medium)

You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.
Return true if you can reach the last index starting from index 0, or false otherwise.

## Jump Game II (Medium)

You are given an array of integers nums, where nums[i] represents the maximum length of a jump towards the right from index i. For example, if you are at nums[i], you can jump to any index i + j where:
j <= nums[i]
i + j < nums.length
You are initially positioned at nums[0].
Return the minimum number of jumps to reach the last position in the array (index nums.length - 1). You may assume there is always a valid answer.

## Merge Triplets to Form Target (Medium)

You are given a 2D array of integers triplets, where triplets[i] = [ai, bi, ci] represents the ith triplet. You are also given an array of integers target = [x, y, z] which is the triplet we want to obtain.
To obtain target, you may apply the following operation on triplets zero or more times:
Choose two different triplets triplets[i] and triplets[j] and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
* E.g. if triplets[i] = [1, 3, 1] and triplets[j] = [2, 1, 2], triplets[j] will be updated to [max(1, 2), max(3, 1), max(1, 2)] = [2, 3, 2].
Return true if it is possible to obtain target as an element of triplets, or false otherwise.