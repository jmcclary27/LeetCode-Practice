# Descriptions and any additional notes for every questions written below

## Valid Palindrome (Easy)

Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Idea: We want to create two pointers, one at the beginning of the string and one at the end. We then loop until the two pointers meet, checking if the characters at each index are equal along the way. We also create a separate function to check if each character is within the alphanumeric guidelines given. This has a runtime complexity of O(n) and a space complexity of O(1)

## Two Integer Sum II (Medium)

Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
There will always be exactly one valid solution.
Your solution must use O(1) additional space.

Idea: Create two pointers at the beginning and end of the array, and loop until the two indexs meet. Check if the numbers at those indexes add to target, if they do, return a list of those indexes plus one. Since the array is sorted, if the sum is less than target, we just increment our first pointer, and if it is greater, we decrement our second pointer. With this method, we solve the problem in O(n) runtime complexity and O(1) space complexity.