# Leetcode 342
# Power of Four

# 利用4的乘方的二进制特点。In Python the precedence of bitwise operators are higher than boolean operators, but lower than addition and subtraction. not > and > xor > or.

# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
#
# Example:
# Given num = 16, return true. Given num = 5, return false.
#
# Follow up: Could you solve it without loops/recursion?

# trivial
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        while num % 4 == 0:
            num /= 4
        if num == 1:
            return True
        else:
            return False
