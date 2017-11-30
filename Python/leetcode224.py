# Basic Calculator

# @southpenguin
# left to right; record sign; use stack only for parentheses
# or shunting yard

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

# shunting yard
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = []
        ops = []
        i = 0
        while i < len(s):
            if ord('0') <= ord(s[i]) <= ord('9'):
                curNum = 0
                while i < len(s) and ord('0') <= ord(s[i]) <= ord('9'):
                    curNum = 10 * curNum + int(s[i])
                    i += 1
                nums.append(curNum)
                continue
            if s[i] in '+-':
                if s[i] == '-': # handle negative number
                    j = i - 1
                    while j >= 0 and s[j] == ' ':
                        j -= 1
                    if j == -1 or s[j] == '(':
                        nums.append(0)
                while ops and ops[-1] != '(':
                    nums.append(self.applyOp(ops.pop(), nums.pop(), nums.pop()))
                ops.append(s[i])
            elif s[i] == '(':
                ops.append(s[i])
            elif s[i] == ')':
                while ops[-1] != '(':
                    nums.append(self.applyOp(ops.pop(), nums.pop(), nums.pop()))
                ops.pop()
            i += 1
        while ops:
            nums.append(self.applyOp(ops.pop(), nums.pop(), nums.pop()))
        return nums[0]

    def applyOp(self, op, b, a):
        if op == '+':
            return a + b
        if op == '-':
            return a - b

# powerful version supporting +-*/() using shunting yard
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = []
        ops = []
        i = 0
        while i < len(s):
            if ord('0') <= ord(s[i]) <= ord('9'):
                curNum = 0
                while i < len(s) and ord('0') <= ord(s[i]) <= ord('9'):
                    curNum = 10 * curNum + int(s[i])
                    i += 1
                nums.append(curNum)
                continue
            if s[i] in '+-*/':
                if s[i] == '-': # handle negative number
                    j = i - 1
                    while j >= 0 and s[j] == ' ':
                        j -= 1
                    if j == -1 or s[j] == '(':
                        nums.append(0)
                # BUG: while ops and self.higher(s[i], ops[0]):
                while ops and ops[-1] != '(' and not self.higher(s[i], ops[-1]):
                    nums.append(self.applyOp(ops.pop(), nums.pop(), nums.pop()))
                ops.append(s[i])
            elif s[i] == '(':
                ops.append(s[i])
            elif s[i] == ')':
                # BUG: while ops[0] != '(':
                while ops[-1] != '(':
                    nums.append(self.applyOp(ops.pop(), nums.pop(), nums.pop()))
                ops.pop()
            i += 1
        while ops:
            nums.append(self.applyOp(ops.pop(), nums.pop(), nums.pop()))
        return nums[0]

    def higher(self, op1, op2):
        # BUG: return op1 in ['*/'] and op2 in ['+-']
        return op1 in '*/' and op2 in '+-'

    def applyOp(self, op, b, a):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            return float(a) / b




# @southpenguin
# left to right; record sign; use stack only for parentheses
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
