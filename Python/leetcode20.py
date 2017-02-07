# Valid Parentheses

# stack

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        valid = {'()', '[]', '{}'}
        for c in s:
            if c in ')]}':
                if stack == [] or not stack.pop() + c in valid:
                    return False
            else:
                stack.append(c)
        return stack == []

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stack = []
        start = {'(': 1, '[': 2, '{': 3}
        end = {')': 1, ']': 2, '}': 3}
        for c in s:
            if c in '({[':
                stack.append(c)
            elif len(stack) == 0 or start[stack.pop()] != end[c]:
                return False

        if len(stack) == 0:
            return True
        else:
            return False
