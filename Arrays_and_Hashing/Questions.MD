# Descriptions and any additional notes for every question written below

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

## Top K Frequent Elements (Medium)

Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Idea: In this solution, we use bucket sort in kind of an untraditional way. We will create a 2D array, where the indices represent the frequency, and the elements at that index are the numbers that occur that many times. We will do this by creating a dictionary, and then looping through nums, adding the numbers and updating their frequency to the dictionary along the way. We will then loop through the dictionary, putting them into their proper bucket. In this 2D array, the elements at the end will have occurred the most times, so to get the top k elements, we loop through the 2D arrray, starting at the end, and output the last k elements. By using bucket sort instead of a more traditional way, like a min heap, we will have shaved our runtime complexity down from O(nlogn) to big O(n), and our space complexity from O(n + k) to O(n)

## Encode and Decode Strings (Medium)

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
Please implement encode and decode.

Idea: I like this one a lot because there are plenty of ways you can encode and decode this. We just want to try to make them both functions as efficient as possible, which for this problem, is O(m + n) for space and O(n) runtime complexity. For this problem, we are going to keep track of the words sizes during the encode process, to make the decode process nice and easy. During the encode process, we create a list of each strings size, and then turn those sizes into strings, and add them to our final string with commas separating them. After the final size, we add a separator to our string (we used # in this example) to signal when the sizes end and the string begin. We will then just add all the strings to our final string. Now that the strings are encoded into one string, we will now decode it back to its original form. The first step will be to loop through the beginning of the string, storing each size to a list of sizes, until we finally hit our separator. From there, we will add our words to our final list by indexing using our sizes we figured out earlier.

## Products of Array Except Self (Medium)

Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.
Follow-up: Could you solve it in O(n) time without using the division operation?

Idea: Initially, the easiest way to solve this in O(n) time would be to multiply all the numbers together, and then divide that number by the number at each index. This question is trying to challenge us by seeing if we can come up with another way to do it. We are supposed to use a trick called a prefix and postfix product. Essentially, the idea is to have an array of the products for every number before the current index, and an array of the products for every number after the position, and then multiply the two arrays together. I took this one step further, by doing this entire process in our final output array so that the extra space created by making two arrays is saved. I stored all the prefix products into the results array, and then I created a variable to store the current suffix products, and looped through the array backwards, multiplyinh by that suffix product number. Overall, this strategy is still O(n) for runtime and space complexity, but it is a little more optimized than the NeetCode answer.

## Valid Sudoku (Medium)

You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false
Note: A board does not need to be full or be solvable to be valid.

Idea: The idea is to create three arrays, one for storing rows, one for columns, and one for the sqaures. We do this by looping through each element (row major) and adding the element to the row and column list by its row and column index. For the sqaures, we divide its row and column indexes (truncated) to find what square it is in. This solution is O(n^2) for both time and space complexity.