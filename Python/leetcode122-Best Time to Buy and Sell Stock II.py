# LeetCode 122
# Best Time to Buy and Sell Stock II

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices) - 1):
            diff = prices[i + 1] - prices[i]
            if diff > 0:
                profit += diff
        return profit
            
