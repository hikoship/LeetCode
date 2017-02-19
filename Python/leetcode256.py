# Paint House

# DP

# There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
#
# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.
#
# Note:
# All costs are positive integers.

# inplace
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if costs == []:
            return 0
        for i in range(1, len(costs)):
            for j in range(3):
                costs[i][j] += min(res[i - 1][(j + 1) % 3], res[i - 1][(j + 2) % 3])
        return min(costs[-1])

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if costs == []:
            return 0
        res = [[0] * 3 for _ in range(len(costs))]
        for i in range(3):
            res[0][i] = costs[0][i]
        for i in range(1, len(costs)):
            for j in range(3):
                res[i][j] = costs[i][j] + min(res[i - 1][(j + 1) % 3], res[i - 1][(j + 2) % 3])
        return min(res[-1])
