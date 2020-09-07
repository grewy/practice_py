class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        power = 31
        while n:
            ret += (n & 1) << power
            power -= 1
            n = n >> 1
        return ret
