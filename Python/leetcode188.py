# Best Time to Buy and Sell Stock IV

# dp: lc122 + lc123

# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0:
            return 0
        if k > len(prices) / 2:
            return self.stock2(prices)
        buy = [float('-inf')] * k
        sell = [0] * k
        for p in prices:
            for i in range(k - 1, 0, -1):
                sell[i] = max(sell[i], buy[i] + p)
                buy[i] = max(buy[i], sell[i - 1] - p)
            sell[0] = max(sell[0], buy[0] + p)
            buy[0] = max(buy[0], -p)
        return sell[k - 1]

    # lc 122
    def stock2(self, prices):
        if prices == []:
            return 0
        res = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                res += prices[i - 1] - buy
                buy = prices[i]
        return res + prices[-1] - buy
