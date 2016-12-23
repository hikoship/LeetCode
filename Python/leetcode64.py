# Minimum Path Sum

# DP. Use only array instead of matrix to record info.

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) ==0 or len(grid[0]) == 0:
            return 0

        res = grid[0]
        for i in range(1, len(grid[0])):
            res[i] += res[i - 1]

        for i in range(1, len(grid)):
            res[0] += grid[i][0]
            for j in range(1, len(grid[0])):
                res[j] = min(res[j], res[j - 1]) + grid[i][j]

        return res[-1]
