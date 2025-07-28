# Descriptions and any additional notes for every questions written below

## Valid Parentheses (Easy)

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
The input string s is valid if and only if:
    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Idea: We will be utilizing a stack to solve this problem. We do this because of a stack having the LIFO property (Last In First Out). Since we are given only three pairings, we can first make a dictionary, with the keys being the open symbols, and their values being the closed symbols. We then loop through the string, and if the current character is an open symbol, we push it to the stack. If the character is closed, we check to see if the top of our stack pairs with it using the dictionary we made earlier, if it does, we pop it off the stack and keep going, if it doesn't we return false. There are also plenty of edge cases here that we watch out for. Using this push and pop method, the code runs in O(n) time and space complexity.

## Minimum Stack (Medium)

Design a stack class that supports the push, pop, top, and getMin operations.
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in O(1) time.

Idea: This question is essentially asking the coder to make a simple stack class. This seems relatively easy at first, however, we are asked to make ALL the functions in constant time. It is intuitive on getMin() to just loop through the stack to find the minimum element, but that does not follow our constant time constraint. The idea I am going with here is to have two stacks. One stack is the normal stack that we will do everything to, and the other stack is a minimum stack, with the values being the minimum value at each point of the regular stack. The idea here is for each time we push an element, we also push the minimum between the end of the minStack and the actual element we are pushing. When we pop the stack, we also pop the minStack. This idea gives us an O(n) space complexity with a O(1) runtime.

## Evaluate Reverse Polish Notation (Medium)

You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
Return the integer that represents the evaluation of the expression.
The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.

Idea: Polish notation is a very weird concept, but once you understand how it works, it becomes clear why a stack is most optimal for this question. The stack allows us to traverse the token list while performing mathematical operations along the way and maintaining the other tokens we have crossed. What we do is loop through the list of tokens and check for one of the four symbols. If we come across one, we pop the last two tokens in the list and perform that mathematical operation. If it is not one of the symbols, we push it to the stack as an integer. This is done in O(n) time and space complexity.

## Daily Temperatures (Medium)

You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Idea: The idea here is to create a stack holding both the temperatures and their index. If we find a temperature greater than our most recent addition to the stack, we loop until there is nothing else in the stack less than this temperature, and we add the difference between the current index and their index to the resulting array. We then add our most recent variables to the stack. This is a O(n) runtime complexity with a O(n) space complexity