# Basic Calculator II

# O(1) space

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
        res = 0
        sign1 = 1 # +-
        sign2 = 1 # */
        i = 0
        curVal = 0
        multiplier = 1
        for x in s:
            if ord('0') <= ord(x) <= ord('9'):
                curVal = 10 * curVal + int(x)
            elif x in '+-':
                res += int((curVal ** sign2) * multiplier * sign1)
                curVal = 0
                multiplier = 1
                sign1 = 1 if x == '+' else -1
                sign2 = 1
            elif x in '*/':
                multiplier = int(multiplier * curVal ** sign2)
                curVal = 0
                sign2 = 1 if x == '*' else -1
        res += int((curVal ** sign2) * multiplier * sign1)
        return res


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        res = 0
        curVal = 0
        multiplier = 1
        op1 = '+'
        op2 = '*'
        while i < len(s):
            if ord('0') <= ord(s[i]) <= ord('9'):
                curVal = 10 * curVal + int(s[i])
            elif s[i] == '+':
                # add mul * cur
            elif s[i] == '*':
                # mul *= cur
        # add cur

                if op2 == '*':
                    multiplier *= curVal
                else:
                    multiplier /= curVal

                if op == '+':
                    res += curVal * multiplier
                    curVal = 0
                    op = s[i]
                    multiplier = 1
                elif op == '-':
                    curVal = 0
                    res -= curVal * multiplier
                    op = s[i]
                    multiplier = 1
                elif op == '*':
                    multiplier *= curVal
                    curVal = 0
                    op = s[i]
                    multiplier = 1
                else:
                    multiplier /= curVal
                    curVal = 0
                    op = s[i]
                    multiplier = 1
                curVal = 0
            elif s[i] in '*/':
                    multiplier *= curVal





            elif s[i] == '-':
                res += curVal * multiplier



                continue




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
