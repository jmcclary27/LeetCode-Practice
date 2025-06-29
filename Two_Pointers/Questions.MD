# Descriptions and any additional notes for every questions written below

## Valid Palindrome (Easy)

Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Idea: We want to create two pointers, one at the beginning of the string and one at the end. We then loop until the two pointers meet, checking if the characters at each index are equal along the way. We also create a separate function to check if each character is within the alphanumeric guidelines given. This has a runtime complexity of O(n) and a space complexity of O(1)