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
            res[i1][i2] =  1 + min(self.f(word1, i1, word2, i2 + 1, res), self.f(word1, i1 + 1, word2, i2, res), self.f(word1, i1 + 1, word2, i2 + 1, res))
        return res[i1][i2]
