class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack or stack[-1][0] != char:
                stack.append((char, 1))
            else:
                counter = stack[-1][1]
                if counter + 1 == k:
                    for i in range(counter):
                        stack.pop()
                else:
                    stack.append((char, counter + 1))
        
        res = ""
        for i in range(len(stack)):
            res += stack[i][0]
        return res