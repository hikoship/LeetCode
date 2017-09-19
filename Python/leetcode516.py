# Longest Palindromic Subsequence

# DP

# Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
# Input:
#
# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input:
#
# "cbbd"
# Output:
# 2
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            # to pass some large corner cases
            return len(s)
        res = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            res[i][i] = 1
        for i in range(1, len(s)):
            for j in range(len(s) - i):
                if (s[j] == s[i + j]):
                    res[j][i + j] = max(res[j][i + j - 1], res[j + 1][i + j], res[j + 1][i + j - 1] + 2)
                else:
                    res[j][i + j] = max(res[j][i + j - 1], res[j + 1][i + j])
        return res[0][-1]
