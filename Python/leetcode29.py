# Divide Two Integers

# binary search & bit manipulation

# Divide two integers without using multiplication, division and mod operator.
#
# If it is overflow, return MAX_INT.

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        negative = False
        if dividend < 0:
            dividend = -dividend
            negative = not negative
        if divisor < 0:
            divisor = -divisor
            negative = not negative

        res = 0
        while dividend >= divisor:
            tmp = divisor
            base = 1
            while tmp << 1 <= dividend:
                tmp <<= 1
                base <<= 1
            res += base
            dividend -= tmp

        if negative:
            res = -res
        if res > 2147483647 or res < -2147483648:
            return 2147483647
        return res
