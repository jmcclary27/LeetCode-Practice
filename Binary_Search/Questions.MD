# Descriptions and any additional notes for every questions written below

## Binary Search (Easy)

You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
Your solution must run in O(logn) time.

Idea: The solution here is to implement the binary search algorithm. The idea behind the algorithm is to create a low and a high index, and the middle of those two is our middle index. We create a loop (our breaking condition is if low becomes greater than high because then we know our target is not in the array), and it is within that loop that we first calculate our middle index. We then check if the number at our middle index is the target, and if it is, return true. Otherwise, we see if our number is lower than target, and if it is, then we update our low index to be mid + 1, because we know it is not on the lower half of the array. If nothing else has executed, that means the number we are at is greater than our target, so we update high to be mid - 1, and continue looping. Since we eleminate half of the array with every iteration, our final runtime is O(log(n)) with a space complexity of O(1).

## Search a 2D Matrix (Medium)

You are given an m x n 2-D integer array matrix and an integer target.
Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.
Can you write a solution that runs in O(log(m * n)) time?

Idea: The idea here is to implement binary search, but with checks and mid calculations for both the rows and the columns. We do thsi by creating a low and a high for both the rows and the columns, and loop until the low for either the rows or columns is greater than the high. We then calculate a mid for both the rows and columns, and see if the number at those indexes is our target and return True if it is. If not, we check if that number is less than target, and if it is, we go to another round of checks. For this round of checks, we see if the last number of the row is less than target, because if it is, we know target is not in that row, and we can update our lowRow to be midRow + 1. If it is not, we update our lowCol to be midCol + 1. Now if that initial check does not execute, (the one checking if the number at our middle row and column is less than target), we know the number at our middle indexes is greater than target, so we can run through our series of checks, with everything flipped. This way runs the code in O(log(m*n) and has a space complexity of O(1).

## Koko Eating Bananas (Medium)

You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.
You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.
Return the minimum integer k such that you can eat all the bananas within h hours.

Idea: The idea here is to use binary search to find our number k. We do this by initially making the low and high numbers for our binary search the lowest and highest possible answers, which is one and the largest pile. We then calculate the number of hours it would take if we ate at a rate of ((low + high) // 2) bananas per hour. We do this by dividing each pile by our middle number and rounding up. If the total number of hours is less than or equal to h, we have found a valid number, and update our result to be our new mid number, and then make high equal to middle - 1. If it is not, we make low = mid + 1, and try again. This solution has a time complexity of O(nlogm) and a space complexity of O(1).