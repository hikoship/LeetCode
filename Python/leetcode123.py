# Best Time to Buy and Sell Stock III

# keep 4 vars
# max balance after first buying
# max balance after first selling
# max balance after second buying
# max balance after second selling


# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

# @qwl5004
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = float('-inf') # max balance after first buying
        sell1 = 0 # max balance after first selling
        buy2 = float('-inf') # max balance after second buying
        sell2 = 0 # max balance after second selling
        for p in prices:
            sell2 = max(sell2, buy2 + p)
            buy2 = max(buy2, sell1 - p)
            sell1 = max(sell1, buy1 + p)
            buy1 = max(buy1, -p)
        return sell2
