# Basic Calculator II

# split to arrays

# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid.
#
# Some examples:
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 / 2 " = 5
# Note: Do not use the eval built-in library function.

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s.replace(' ', '')
        array = self.toArray(s, '+-')
        for i, item in enumerate(array):
            if '*' in item or '/' in item:
                array[i] = self.getRes(self.toArray(item, '*/'))
        return self.getRes(array)

    def toArray(self, s, ops):
        prev = 0
        array = []
        for i, c in enumerate(s):
            if c in ops:
                array.append(s[prev : i])
                array.append(c)
                prev = i + 1
        array.append(s[prev:])
        return array

    def getRes(self, array):
        res = int(array[0])
        i = 1
        while i < len(array):
            if array[i] == '+':
                res += int(array[i + 1])
            elif array[i] == '-':
                res -= int(array[i + 1])
            elif array[i] == '*':
                res *= int(array[i + 1])
            else:
                res /= int(array[i + 1])
            i += 2
        return res
