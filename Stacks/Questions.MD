# Descriptions and any additional notes for every questions written below

## Valid Parentheses (Easy)

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
The input string s is valid if and only if:
    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Idea: We will be utilizing a stack to solve this problem. We do this because of a stack having the LIFO property (Last In First Out). Since we are given only three pairings, we can first make a dictionary, with the keys being the open symbols, and their values being the closed symbols. We then loop through the string, and if the current character is an open symbol, we push it to the stack. If the character is closed, we check to see if the top of our stack pairs with it using the dictionary we made earlier, if it does, we pop it off the stack and keep going, if it doesn't we return false. There are also plenty of edge cases here that we watch out for. Using this push and pop method, the code runs in O(n) time and space complexity.