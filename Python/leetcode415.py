# Add Strings

# equalize length

# Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ''
        l1 = len(num1)
        l2 = len(num2)
        # equalize length
        num1 = '0' * (l2 - l1) + num1
        num2 = '0' * (l1 - l2) + num2
        l = max(l1, l2)
        i = l - 1
        carry = 0
        while (i >= 0):
            tmp = int(num1[i]) + int(num2[i]) + carry
            res = str(tmp % 10) + res
            carry = tmp / 10
            i -= 1
        if (carry == 1):
            res = '1' + res
        return res
