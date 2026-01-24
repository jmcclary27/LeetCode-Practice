class Solution:
    def reverseBits(self, n: int) -> int:
        bi = bin(n)[2:]
        bi = '0' * (32 - len(bi)) + bi
        return int(bi[::-1], 2)