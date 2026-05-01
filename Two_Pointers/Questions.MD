# Descriptions and any additional notes for every questions written below

## Valid Palindrome (Easy)

Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Idea: We want to create two pointers, one at the beginning of the string and one at the end. We then loop until the two pointers meet, checking if the characters at each index are equal along the way. We also create a separate function to check if each character is within the alphanumeric guidelines given. This has a runtime complexity of O(n) and a space complexity of O(1)

## Valid Palindrome II (Easy)

You are given a string s, return true if the s can be a palindrome after deleting at most one character from it.
A palindrome is a string that reads the same forward and backward.
Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

## Merge Strings Alternately (Easy)

You are given two strings, word1 and word2. Construct a new string by merging them in alternating order, starting with word1 — take one character from word1, then one from word2, and repeat this process.
If one string is longer than the other, append the remaining characters from the longer string to the end of the merged result.
Return the final merged string.

## Merge Sorted Array (Easy)

You are given two integer arrays nums1 and nums2, both sorted in non-decreasing order, along with two integers m and n, where:
m is the number of valid elements in nums1,
n is the number of elements in nums2.
The array nums1 has a total length of (m+n), with the first m elements containing the values to be merged, and the last n elements set to 0 as placeholders.
Your task is to merge the two arrays such that the final merged array is also sorted in non-decreasing order and stored entirely within nums1.
You must modify nums1 in-place and do not return anything from the function.

## Remove Duplicates From Sorted Array (Easy)

You are given an integer array nums sorted in non-decreasing order. Your task is to remove duplicates from nums in-place so that each element appears only once.
After removing the duplicates, return the number of unique elements, denoted as k, such that the first k elements of nums contain the unique elements.
Note:
The order of the unique elements should remain the same as in the original array.
It is not necessary to consider elements beyond the first k positions of the array.
To be accepted, the first k elements of nums must contain all the unique elements.
Return k as the final result.

## Valid Word Abbreviations (Easy)

A string can be shortened by replacing any number of non-adjacent, non-empty substrings with their lengths (without leading zeros).
For example, the string "implementation" can be abbreviated in several ways, such as:
"i12n" -> ("i mplementatio n")
"imp4n5n" -> ("imp leme n tatio n")
"14" -> ("implementation")
"implemetation" -> (no substrings replaced)
Invalid abbreviations include:
"i57n" -> (i mplem entatio n, adjacent substrings are replaced.)
"i012n" -> (has leading zeros)
"i0mplementation" (replaces an empty substring)
You are given a string named word and an abbreviation named abbr, return true if abbr correctly abbreviates word, otherwise return false.
A substring is a contiguous non-empty sequence of characters within a string.

## Merge Two 2D Arrays By Summing Values (Easy)

You are given two 2D integer arrays nums1 and nums2.
nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
Each array contains unique ids and is sorted in ascending order by id.
Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:
Only ids that appear in at least one of the two arrays should be included in the resulting array.
Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be 0.
Return the resulting array. The returned array must be sorted in ascending order by id.

## Two Integer Sum II (Medium)

Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
There will always be exactly one valid solution.
Your solution must use O(1) additional space.

Idea: Create two pointers at the beginning and end of the array, and loop until the two indexs meet. Check if the numbers at those indexes add to target, if they do, return a list of those indexes plus one. Since the array is sorted, if the sum is less than target, we just increment our first pointer, and if it is greater, we decrement our second pointer. With this method, we solve the problem in O(n) runtime complexity and O(1) space complexity.

## Rotate Array (Medium)

You are given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

## 3Sum (Medium)

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Idea: The idea here is to sort nums and then enumerate it. The idea from here is simple, if our first pointer is positive, we have gone too far and we break, otherwise we just implement plain old two sum. Since we have to loop for the first pointer and then loop again for l and r, the runtime complexity is O(n^2) and has a space complexity of O(n) due to our resulting array

## Adding Spaces To String (Medium)

You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.
For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
Return the modified string after the spaces have been added.

## Container With Most Water (Medium)

You are given an integer array heights where heights[i] represents the height of the ith bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Idea: This problem is easily solved using the two pointer method. We will create two pointers, pointing to the beggining and end of the array, and loop until the two pointers meet. We will calculate the current area of the container by multiplying the difference between our two pointers by the height of the smaller bar at one of our two pointers. We also have a variable keeping track of the largest area, and we update this variable to the current area, only if the current area is bigger. Then, we check if the height at our first pointer is larger than the height at our second pointer, and if it is, we decrement our second pointer, otherwise, we increment our first pointer. Finally return our variable keeping track of the largest area. This has a time complexity of O(n) and a space complexity of O(1).

## Trapping Rain Water (Hard)

You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.
Return the maximum area of water that can be trapped between the bars.

Idea: The idea here is to implement two pointer with two variables keeping track of the max height seen by each of the two pointers (we call them leftMax and rightMax). So we start like any normal two pointer question, creating an l and r and looping until they meet, but we also have leftMax equal to the height at l and same thing for rightMax with r. Now what we do is find the minimum between the two maxes because we can only store water up to the lower point. If l is the minimum, we increment l, and if it is r we decrement r. Then what we do is compare if the new height is greater than the max on that side, and if it is, it becomes the new max. We then add the difference between the max and the current height to our result. This works because if our new height does become the new max, we know no water can be stored at that point right now, and if it is smaller, well then we know water can. This solution is O(n) runtime with a O(1) space complexity.