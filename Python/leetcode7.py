# Reverse Integer

# easy

# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output:  321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        res = 0
        if x < 0:
            sign = -1
            x = abs(x)
        res = 0
        while x:
            res = res * 10 + x % 10
            x /= 10
        return 0 if res > 2 ** 31 - 1 else res * sign
