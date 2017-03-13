# Distinct Subsequences

# res[i][j]: distinct subsequences when for s[:i] and t[:j]

# Given a string S and a string T, count the number of distinct subsequences of T in S.
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# Here is an example:
# S = "rabbbit", T = "rabbit"
#
# Return 3.

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        M = len(s)
        N = len(t)
        res = [[1] * (N + 1) for _ in range(M + 1)]
        for j in range(1, N + 1):
            res[0][j] = 0
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                res[i][j] = res[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    res[i][j] += res[i - 1][j - 1]
        return res[M][N]
