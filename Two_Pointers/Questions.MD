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

## Container With Most Water (Medium)

You are given an integer array heights where heights[i] represents the height of the ith bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Idea: This problem is easily solved using the two pointer method. We will create two pointers, pointing to the beggining and end of the array, and loop until the two pointers meet. We will calculate the current area of the container by multiplying the difference between our two pointers by the height of the smaller bar at one of our two pointers. We also have a variable keeping track of the largest area, and we update this variable to the current area, only if the current area is bigger. Then, we check if the height at our first pointer is larger than the height at our second pointer, and if it is, we decrement our second pointer, otherwise, we increment our first pointer. Finally return our variable keeping track of the largest area. This has a time complexity of O(n) and a space complexity of O(1).