# Triangle

# 动态规划迭代的时候从后往前，防止覆盖数据；头和尾单独计算

# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        l = len(triangle)
        res = [triangle[0][0]] + [0] * (l - 1)
        for i in range(1, l):
            resHead = res[0] + triangle[i][0]
            resTail = res[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                res[j] = min(res[j - 1], res[j]) + triangle[i][j]
            res[0] = resHead
            res[i] = resTail
        return min(res)
