# Coin Change

# dp saves the world!!!

# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
#
# Example 2:
# coins = [2], amount = 3
# return -1.
#
# Note:
# You may assume that you have an infinite number of each kind of coin.

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return -1 if dp[amount] == amount + 1 else dp[amount]



# TLE; didn't cut branches when cur > res
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # coins.sort(reverse=True) sort makes it slower
        cache = {}
        return self.dfs(coins, amount, cache)

    def dfs(self, coins, amount, cache):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if amount in cache:
            return cache[amount]
        res = float('inf')
        for c in coins:
            tmp = self.dfs(coins, amount - c, cache)
            if tmp >= 0:
                res = min(res, tmp + 1)
        if res == float('inf'):
            res = -1
        cache[amount] = res
        return res
