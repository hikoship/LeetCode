# 01 Matrix

# easy BFS

# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
# Example 1:
# Input:
#
# 0 0 0
# 0 1 0
# 0 0 0
# Output:
# 0 0 0
# 0 1 0
# 0 0 0
# Example 2:
# Input:
#
# 0 0 0
# 0 1 0
# 1 1 1
# Output:
# 0 0 0
# 0 1 0
# 1 2 1
# Note:
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        M = len(matrix)
        N = len(matrix[0])
        points = []
        res = [[float('inf')] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    points.append((i, j))
                    res[i][j] = 0
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while points:
            newPoints = []
            for p in points:
                for d in dirs:
                    x = p[0] + d[0]
                    y = p[1] + d[1]
                    if 0 <= x < M and 0 <= y < N and res[x][y] == float('inf'):
                        newPoints.append((x, y))
                        res[x][y] = res[p[0]][p[1]] + 1
            points = newPoints
        return res
