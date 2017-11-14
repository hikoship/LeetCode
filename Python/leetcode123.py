class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = float('-inf')
        sell1 = 0
        minIn2 = float('inf')
        maxDiff2 = 0
        for p in prices:
            minIn1 = min(minIn1, p)
            maxDiff1 = max(maxDiff1, p - minIn1)
            minIn2 = min(minIn2, p + minIn1)
            maxDiff2 = max(maxDiff1, p - minIn2 + maxDiff1)
        return maxDiff2
