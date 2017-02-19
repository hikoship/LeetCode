# Edit Distance

# DP

# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
#
# You have the following 3 operations permitted on a word:
#
# a) Insert a character
# b) Delete a character
# c) Replace a character

# iterative
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        M = len(word1)
        N = len(word2)
        res = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M + 1):
            res[i][0] = i
        for j in range(N + 1):
            res[0][j] = j
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if word1[i - 1] == word2[j - 1]:
                    res[i][j] = res[i - 1][j - 1]
                else:
                    res[i][j] = 1 + min(res[i - 1][j - 1], res[i - 1][j], res[i][j - 1])
        return res[M][N]

# recursive, beat 99%
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = [[-1] * len(word2) for _ in range(len(word1))]
        return self.f(word1, 0, word2, 0, res)

    def f(self, word1, i1, word2, i2, res):
        if i1 == len(word1):
            return len(word2) - i2
        if i2 == len(word2):
            return len(word1) - i1
        if res[i1][i2] != -1:
            return res[i1][i2]
        if word1[i1] == word2[i2]:
            res[i1][i2] = self.f(word1, i1 + 1, word2, i2 + 1, res)
        else:
            res[i1][i2] = 1 + min(self.f(word1, i1, word2, i2 + 1, res), self.f(word1, i1 + 1, word2, i2, res), self.f(word1, i1 + 1, word2, i2 + 1, res))
        return res[i1][i2]
