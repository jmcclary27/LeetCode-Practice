# Descriptions and any additional notes for every questions written below

## Best Time to Buy and Sell Stock (Easy)

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Idea: The idea here is to establish two pointers at the first two indexes and loop until that second pointer has made it through the whole array. In the loop, we check if the price at the right pointer is greater than the price at the left pointer, and if it is, we find their difference and assign the max profit variable to whichever is greater. If not, we move the left pointer up to the right pointer. We increment r at the end of each loop. We then return our max profit. This executes in O(n) time and O(1) space.

## Longest Substring Without Repeating Characters (Medium)

Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.

Idea: The idea here is to create a set for each letter in the string. We loop through the entire string and if the letter at the index of our second pointer is in the character set, we have found a duplicate and remove everything from the set one by one, all while incrementing l. We then find how many times l was incremented (which is the length of the substring) and see if it is greater than our current max length. After looping through every letter, we return the max length of substring in O(n) time and O(m) space, where m is the number of unique characters.

## Permutation in String (Medium)

You are given two strings s1 and s2.
Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.
Both strings only contain lowercase letters.