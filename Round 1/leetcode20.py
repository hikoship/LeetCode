# LeetCode 20
# Valid Parentheses

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
