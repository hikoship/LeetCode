# Longest Increasing Path in a Matrix

# DFS + DP

# Given an integer matrix, find the length of the longest increasing path.
#
# From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
#
# Example 1:
#
# nums = [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Return 4
# The longest increasing path is [1, 2, 6, 9].
#
# Example 2:
#
# nums = [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Return 4
# The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        length = 0
        record = [[0] * len(matrix[0]) for _ in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                length = max(length, self.dfs(matrix, record, i, j))
        return length

    def dfs(self, matrix, record, i, j):
        if record[i][j] > 0:
            return record[i][j]
        length = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for d in dirs:
            x = i + d[0]
            y = j + d[1]
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                length = max(length, self.dfs(matrix, record, x, y))
        record[i][j] = length + 1
        return length + 1
