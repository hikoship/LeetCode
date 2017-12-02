# Decode Ways

# Recursion failed

# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        dp = [0] * len(s)
        dp[0] = 0 if s[0] == '0' else 1
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i] = dp[i - 1]
            # BUG: 0 <= int(s[i - 1: i + 1]) <= 26: '01' is invalid
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                dp[i] += 1 if i == 1 else dp[i - 2]
        return dp[-1]
