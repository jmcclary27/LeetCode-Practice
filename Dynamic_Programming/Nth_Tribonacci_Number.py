class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0

        if n < 3: return 1

        first, second, third = 0, 1, 1
        for i in range(3, n+1):
            temp = first + second + third
            first = second
            second = third
            third = temp
        return third