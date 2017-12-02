# Multiply Strings

# directly storing num1[i] * num2[j] to res[i + j + 1].

# Given two numbers represented as strings, return multiplication of the numbers as a string.
#
# Note:
# The numbers can be arbitrarily large and are non-negative.
# Converting the input string to integer is NOT allowed.
# You should NOT use internal library such as BigInteger.

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'

        length1 = len(num1)
        length2 = len(num2)
        res = [0] * (length1 + length2)

        for i in range(length1):
            for j in range(length2):
                res[i + j + 1] += int(num1[i]) * int(num2[j])

        for i in range(length1 + length2 - 1, 0, -1):
            res[i - 1] += res[i] / 10
            res[i] %= 10

        if res[0] == 0:
            res = res[1:]
        return ''.join(map(str, res))



class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        length1 = len(num1)
        length2 = len(num2)
        for i in range(length1 - 1, -1, -1):
            tmpRes = ''
            carry = 0
            for j in range(length2 - 1, -1, -1):
                tmpTmpRes = int(num1[i]) * int(num2[j]) + carry
                carry = tmpTmpRes / 10
                tmpRes += str(tmpTmpRes % 10)
            tmpRes += str(carry)
            res.append(tmpRes) # tmpRes is litte-endian

        # add 0 suffix
        for i in range(len(res)):
            res[i] = ('0' * i + res[i] + '0' * (length1 - i - 1))

        # sum up
        output = ''
        tmpRes = ''
        carry = 0
        for i in range(length1 + length2):
            tmpRes = sum([int(res[j][i]) for j in range(length1)]) + carry
            output = str(tmpRes % 10) + output
            carry = tmpRes / 10
        if carry > 0:
            output = str(carry) + output

        i = 0
        while output[i] == '0' and i < len(output) - 1:
            i += 1

        return output[i:]
