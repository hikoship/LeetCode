# Unique Paths II

# if there is an obstacle, the num is zero.

# Follow up for "Unique Paths":
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
#
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.
#
# Note: m and n will be at most 100.

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        num = [1] * n
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                while i < n:
                    num[i] = 0
                    i += 1
                break
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                num[0] = 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    num[j] = 0
                else:
                    num[j] += num[j - 1]
        return num[-1]
