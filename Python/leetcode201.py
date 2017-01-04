# Bitwise AND of Numbers Range

# Suppose b The leftmost different bit of m and n. Because n is larger than m, the bit of m is 0 and the bit of n is 1.
# m = 0011010XXXXXXXXXXXXX
# n = 0011011XXXXXXXXXXXXX
#           ^
#           b
# Then between m and n, there must be a number k:
# k = 00110110000000000000
# So the bits of AND from m to n are all 0 after the location of b.
# For the bits before b of numbers from m to n, they are all 0011001, so AND result is 0011001.

# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
#
# For example, given the range [5, 7], you should return 4.

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        factor = 0
        while m != n:
            m >>= 1
            n >>= 1
            factor += 1
        return m << factor

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        span = n - m
        mask = 1
        res = 0
        for i in range(31):
            if mask & m and (mask << 1) - (((mask << 1) - 1) & m) > span:
                res |= mask
            mask <<= 1
        return res
