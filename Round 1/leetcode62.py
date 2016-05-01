# LeetCode 62
# Unique Paths

# DP method
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        num = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                num[j] += num[j - 1]
        return num[-1]

'''
Maths method

class Solution(object):
    def combinations(self, x, y):
        if x == 0:
            return 1
        res = y
        for i in range(x - 1):
            y -= 1
            res *= y
        for i in range(x - 1):
            res /= x
            x -= 1
        return res
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.combinations(min(m, n) - 1, m + n - 2)
'''
