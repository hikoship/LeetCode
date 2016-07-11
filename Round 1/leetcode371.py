# Sum of Two Integers

# << is a calculation operator, instead of an assignment operator, while <<= is.

# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
# Example:
# Given a = 1 and b = 2, return 3.

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        res = 0
        c = 0
        mask = 1
        while mask < 1 << 32:
            if a & b & c & mask:
                c = mask << 1
                res |= mask
            elif ~a & ~b & ~c & mask:
                c = 0
            elif a & b & ~c & mask or a & ~b & c & mask or ~a & b & c & mask:
                c = mask << 1
            else:
                c = 0
                res |= mask
            mask <<= 1
        if res > 2147483647:
            res -= 4294967296
        return res
