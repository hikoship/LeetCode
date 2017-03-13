# Interleaving String

# res[i][j]: whether s3[:i + j] can be composed by s1[:i] and s2[:j]

# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
#
# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",
#
# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        N1 = len(s1)
        N2 = len(s2)
        if N1 + N2 != len(s3):
            return False
        res = [[True] * (N2 + 1) for _ in range(N1 + 1)]
        for i in range(1, N1 + 1):
            res[i][0] = s1[i - 1] == s3[i - 1] and res[i - 1][0]
        for j in range(1, N2 + 1):
            res[0][j] = s2[j - 1] == s3[j - 1] and res[0][j - 1]
        for i in range(1, N1 + 1):
            for j in range(1, N2 + 1):
                res[i][j] = s3[i + j - 1] == s1[i - 1] and res[i - 1][j] or s3[i + j - 1] == s2[j - 1] and res[i][j - 1]
        return res[N1][N2]
