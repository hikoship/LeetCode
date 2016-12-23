# Best Time to Buy and Sell Stock with Cooldown

# No idea at all. Use state machine.

# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
#
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:
#
# prices = [1, 2, 3, 0, 2]
# maxProfit = 3
# transactions = [buy, sell, cooldown, buy, sell]

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # status 0: cooldown. next: s0 / s1
        # status 1: hold. next: s1 / s2
        # status 2: sell. next: s0
        l = len(prices)
        if l < 2:
            return 0
        s0 = [0]
        s1 = [-prices[0]]
        s2 = [0]
        for i in range(1, l):
            s0.append(max(s0[i - 1], s2[i - 1]))
            s1.append(max(s0[i - 1] - prices[i], s1[i - 1]))
            s2.append(s1[i - 1] + prices[i])
        return max(s0[-1], s2[-1])
