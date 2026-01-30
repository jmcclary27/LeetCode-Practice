# Descriptions and any additional notes for every questions written below

## Climbing Stairs (Easy)

You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.
Return the number of distinct ways to climb to the top of the staircase.

Idea: The idea here is to use a space optimized tabulation method, because as you'll see in a second, we don't actually need a table to keep tabs of everything. When thinking about this problem, I chose to break it down into a subproblem, and when doing so, I figured the best way was to first find the answer for zero stairs, and then one stair, and then two, all the way to n stairs. I was first solving this with a traditional tabular method, but as I was checking the test cases, I quickly realized the answer to this problem is a fibonnacci sequence. The reason why is there are only two possible ways to get to the final answer, you can get there by taking two steps, or get there by taking one step. If you take one step to get to n stairs, it has the exact amount of possible combinations as n-1 does, and if you take two steps, it has the same amount of possible combinations as n-2. In other words, the amount of possible ways to climb n stairs is the amount of possible ways at n-1 plus the amount of possible ways at n-2. So I looped from 1 to n, keeping track of the previous two variables and adding them along the way, solving this problem in O(n) runtime complexity and O(1) space complexity.

## Min Cost Climbing Stairs (Easy)

You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.
You may choose to start at the index 0 or the index 1 floor.
Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.

Idea: The idea here is to do a space optimized tabular method, where instead of creating a new array, I edit the cost array in place. I created a variable called currMin, that keeps track of the minimum between the last two elements. I then loop through the cost array, adding the currMin to each element, and then finding the new currMin, so by the time I reach the end of cost, the minimum of the final two elements will have the cheapest possible path. This runs in O(n) runtime complexity and O(1) space complexity.

## House Robber (Medium)

You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.
You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.
Return the maximum amount of money you can rob without alerting the police.

Idea: We are once again using a tabular space optimized method to solve this problem. The trick to this one is to track both the current max profit, and then the max profit from two houses back. As we loop through the houses, we add the back max to the current number, and at the end return out current maximum. This runs in O(n) runtime complexity and O(1) space complexity.

## House Robber II (Medium)

You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a circle, i.e. the first house and the last house are neighbors.
You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.
Return the maximum amount of money you can rob without alerting the police.

Idea: The idea here is to use the algorithm in House Robber I with a little bit of a twist. Read the above problem for those details. Since the trick to this problem is that the array is cyclic, we have to manipulate our original algorithm. Since the first and last numbers are neighbors, we know that we can only pick one, so the trick is to run our original algorithm on the array without the first element, and again without the last, and take the greater of the two. This runs in O(n) runtime complexity and O(1) space.

## Decode Ways (Medium)

A string consisting of uppercase english characters can be encoded to a number using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode a message, digits must be grouped and then mapped back into letters using the reverse of the mapping above. There may be multiple ways to decode a message. For example, "1012" can be mapped into:
"JAB" with the grouping (10 1 2)
"JL" with the grouping (10 12)
The grouping (1 01 2) is invalid because 01 cannot be mapped into a letter since it contains a leading zero.
Given a string s containing only digits, return the number of ways to decode it. You can assume that the answer fits in a 32-bit integer.

Idea: The idea here is to once again use a tablular space optimized method. There are some edge cases to watch out for, but the general idea is it is once again a fibonnaci sequence for the possible ways to go about this. The only difference this time is 0's can cause some weird behaviour. The time complexity for this problem is O(n) for runtime and O(1) for space complexity. 

## Coin Change (Medium)

You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.
Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.
You may assume that you have an unlimited number of each coin.

Idea: The idea here is to use tabulation to calculate the least amount of coins starting at amount = 0 all the way to amount = n. To find the least amount of coins for amount = k, we start with a coin called c, which now gives us a total of one coin. We then calculate the least amount of coins for the amount k - c, which is how much we have left. By the time we get up to k = n, we will already know the least amount of coins for any k - c. This code runs in O(n * t), where t is the given amount, and O(t) space.

## Maximum Product Subarray (Medium)

Given an integer array nums, find a subarray that has the largest product within the array and return it.
A subarray is a contiguous non-empty sequence of elements within an array.
You can assume the output will fit into a 32-bit integer.