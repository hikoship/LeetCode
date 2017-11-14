# Best Time to Buy and Sell Stock II

# easy

# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
#

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        res = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                res += prices[i - 1] - buy
                buy = prices[i]
        return res + prices[-1] - buy



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
