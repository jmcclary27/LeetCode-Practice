# Descriptions and any additional notes for every questions written below

## Contains Duplicate (Easy)

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Idea: Create a set from the elements within Nums, and then compare the length of the set to the length of Nums. If the lengths are the same, then there isn't and duplicate and we return false. If the length of the set is smaller than the length of Nums, then there is a duplicate and we return true. This has a big O(n) runtime complexity and a O(n) space complexity.

## Valid Anagram (Easy)

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Idea: Create two empty dictionaries, one for string s and one for string t. Use a for loop to loop through the two strings (also have a base case where if the two strings are not equal then return false) and as you loop through the strings, add each letter to their respectivce dictionary, and have their values be an updating counter of the number of occurences of the keys (the letters). At the end, see if the two dictionaries are equal, if they are, return true, if not, return false. This method has a O(n + m) runtime (n and m being the lengths of strings s and t), and a O(1) space complexity (since there are only 26 letters).

## Two Sum (Easy)

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Idea: Create an empty dictionary and then loop through nums. Subtract The target value by the current number, and see if this difference is in our dictionary. If it is in our dictionary, return the value of the key number in the dictionary (which is its index in nums) and return the current index. If it is not in our dictionary, add the current number to the dictionary with its index being its value. This solution has a O(n) runtime complexity and a O(n) space complexity.

## Group Anagram (Medium)

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Idea: Create an empty dictionary to start out with, and then loop through the strings in the list. Create a count array for each string, and then increment through the letters of each string, updating the values at the letters corresponding index. Use ord() to get the index of each letter. ord() gets the ASCII values of characters, so if you subtract the characters by the ASCII value of a, we will be given a value between 0 and 25 which we then use for indexing. After we loop through the string, we convert its count array to a tuple, and add it to our dictionary, with its value being the word. Since we use append to add the value, if there is another word with a matching count array, it will get added to the same key. We then return the values of our dictionary converted to a list, so we now have a list of lists, grouped by which strings are anagrams. This time complexity is O(m * n) (m being the number of strings and n being the length of the longest string), and the space complexity is O(m * n) (output) with O(m) extra space (count arrays).