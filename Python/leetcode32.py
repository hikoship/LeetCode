# Longest Valid Parentheses

# 1. stack
# 2. DP: res[i] = the length of valid substring ending with i. For i + 1, Find the left index.

# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
#
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

# my solution without using stack! cool!
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * len(s)
        res = 0
        for i in range(1, len(s)):
            leftIdx = i - dp[i - 1] - 1 # the substring between leftIdx and i is a valid pair string
            if s[i] == ')' and leftIdx >= 0 and s[leftIdx] == '(':
                dp[i] = dp[i - 1] + 2
                if i >= dp[i]:
                    dp[i] += dp[i - dp[i]] # concatenate
                res = max(res, dp[i])
        return res
    

# stack
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        left = -1
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack == []:
                    left = i
                else:
                    stack.pop()
                    if stack:
                        res = max(res, i - stack[-1])
                    else:
                        res = max(res, i - left)
        return res
