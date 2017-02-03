# Factor Combinations

# DFS

# Numbers can be regarded as product of its factors. For example,
#
# 8 = 2 x 2 x 2;
#   = 2 x 4.
# Write a function that takes an integer n and return all possible combinations of its factors.
#
# Note:
# You may assume that n is always positive.
# Factors should be greater than 1 and less than n.
# Examples:
# input: 1
# output:
# []
# input: 37
# output:
# []
# input: 12
# output:
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ]
# input: 32
# output:
# [
#   [2, 16],
#   [2, 2, 8],
#   [2, 2, 2, 4],
#   [2, 2, 2, 2, 2],
#   [2, 4, 4],
#   [4, 8]
# ]

class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # WRONG: return self.f(2, n)
        res = self.f(2, n)
        res.remove([n])
        return res

    def f(self, low, n):
        high = int(math.sqrt(n))
        # WRONG: res = []
        res = [[n]]
        for i in range(low, high + 1):
            if n % i == 0:
                for facs in self.f(i, n / i):
                    res.append([i] + facs)
        return res
