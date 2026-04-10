# Descriptions and any additional notes for every questions written below

## Valid Parentheses (Easy)

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
The input string s is valid if and only if:
    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Idea: We will be utilizing a stack to solve this problem. We do this because of a stack having the LIFO property (Last In First Out). Since we are given only three pairings, we can first make a dictionary, with the keys being the open symbols, and their values being the closed symbols. We then loop through the string, and if the current character is an open symbol, we push it to the stack. If the character is closed, we check to see if the top of our stack pairs with it using the dictionary we made earlier, if it does, we pop it off the stack and keep going, if it doesn't we return false. There are also plenty of edge cases here that we watch out for. Using this push and pop method, the code runs in O(n) time and space complexity.

## Baseball Game (Easy)

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
Given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
An integer x: Record a new score of x.
'+': Record a new score that is the sum of the previous two scores.
'D': Record a new score that is the double of the previous score.
'C': Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.
Note: The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

## Implement Stack Using Queues (Easy)

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
Implement the MyStack class:
void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:
You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

## Implement Queue Using Stacks (Easy)

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
Implement the MyQueue class:
void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:
You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

## Minimum Stack (Medium)

Design a stack class that supports the push, pop, top, and getMin operations.
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in O(1) time.

Idea: This question is essentially asking the coder to make a simple stack class. This seems relatively easy at first, however, we are asked to make ALL the functions in constant time. It is intuitive on getMin() to just loop through the stack to find the minimum element, but that does not follow our constant time constraint. The idea I am going with here is to have two stacks. One stack is the normal stack that we will do everything to, and the other stack is a minimum stack, with the values being the minimum value at each point of the regular stack. The idea here is for each time we push an element, we also push the minimum between the end of the minStack and the actual element we are pushing. When we pop the stack, we also pop the minStack. This idea gives us an O(n) space complexity with a O(1) runtime.

## Asteroid Collision (Medium)

You are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

## Evaluate Reverse Polish Notation (Medium)

You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
Return the integer that represents the evaluation of the expression.
The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.

Idea: Polish notation is a very weird concept, but once you understand how it works, it becomes clear why a stack is most optimal for this question. The stack allows us to traverse the token list while performing mathematical operations along the way and maintaining the other tokens we have crossed. What we do is loop through the list of tokens and check for one of the four symbols. If we come across one, we pop the last two tokens in the list and perform that mathematical operation. If it is not one of the symbols, we push it to the stack as an integer. This is done in O(n) time and space complexity.

## Generate Parentheses (Medium)

You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Idea: The idea here is to use recrusive backtracking to find all possible combinations of the parentheses. We do this by defining our result list and our stack, before defining a nested function for the backtracking. The function will keep track of how many open and closed parenthesis we have. If we have n open and n closed parenthesis we add the stack to res and return. If we have less than n open parentheses, we add one to the stack and recall backtracking, this time with one more open parentheses. We do the same process for the closed parenthesis. After the calls, we pop the stack, which is where our backtracking process comes into play. In total, this idea is O((4^n)/root(n)) time complexity with O(n) space complexity

## Daily Temperatures (Medium)

You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Idea: The idea here is to create a stack holding both the temperatures and their index. If we find a temperature greater than our most recent addition to the stack, we loop until there is nothing else in the stack less than this temperature, and we add the difference between the current index and their index to the resulting array. We then add our most recent variables to the stack. This is a O(n) runtime complexity with a O(n) space complexity

## Car Fleet (Medium)

There are n cars traveling to the same destination on a one-lane highway.
You are given two arrays of integers position and speed, both of length n.
position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.
A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.
A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.
If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.
Return the number of different car fleets that will arrive at the destination.

Idea: The idea here is to sort the position array and to loop through it backwards (or sort the array in decreasing order). In the loop, we calculate the time it will take for the ith car to reach target, and if it is less than or equal to the top of the stack, then we know that car will be apart of the fleet, so we change its time to the time of the top of the stack, and make it the new top. If the time is greater than the top of the stack. We empty the stack, then add the new time to the stack, and increment our result by one. This solution is O(nlogn) for time complexity (because of sorting) and O(n) for space complexity.