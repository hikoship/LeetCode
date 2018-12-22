# memorization
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        return self.dp(1, n, cache)

    def dp(self, low, high, cache):
        if low >= high:
            return 0
        if (low, high) in cache:
            return cache[(low, high)]
        res = float('inf')
        for i in range(low, high + 1):
            res = min(res, max(self.dp(low, i - 1, cache), self.dp(i + 1, high, cache)) + i)
        cache[(low, high)] = res
        return res
