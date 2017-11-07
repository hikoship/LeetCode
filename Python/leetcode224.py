# Basic Calculator

# @southpenguin
# left to right; record sign; use stack only for parentheses

# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
#
# You may assume that the given expression is always valid.
#
# Some examples:
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23
# Note: Do not use the eval built-in library function.

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        num = 0
        sign = 1
        stack = []
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            elif '0' <= s[i] <= '9':
                num = 10 * num + int(s[i])
            else:
                res += sign * num
                num = 0
                if s[i] == '+':
                    sign = 1
                elif s[i] == '-':
                    sign = -1
                elif s[i] == '(':
                    stack.append(res)
                    stack.append(sign)
                    res = 0
                    sign = 1
                else:
                    res *= stack.pop()
                    res += stack.pop()
        return res + sign * num
