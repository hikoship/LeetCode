# Range Sum Query 2D - Mutable

# 2D trie

# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
#
# Range Sum Query 2D
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.
#
# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10
# Note:
# The matrix is only modifiable by the update function.
# You may assume the number of calls to update and sumRegion function is distributed evenly.
# You may assume that row1 ≤ row2 and col1 ≤ col2.

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.M = len(matrix)
        if self.M == 0:
            return
        self.N = len(matrix[0])
        self.tree = [[0] * (self.N + 1) for _ in range(self.M + 1)]
        self.nums = [[0] * self.N for _ in range(self.M)]
        for i in range(self.M):
            for j in range(self.N):
                self.update(i, j, matrix[i][j])


    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[row][col]
        self.nums[row][col] = val
        # BUG: FATAL BUG!!!:
        # i += 1
        # j += 1
        # while i <= self.M:
        #     while j <= self.N:
        #         self.tree[i][j] += diff
        #         j += j & (-j)
        #     i += i & (-i)
        i = row + 1
        while i <= self.M:
            j = col + 1
            while j <= self.N:
                self.tree[i][j] += diff
                j += j & (-j)
            i += i & (-i)


    def getSum(self, row, col):
        res = 0
        # BUG: FATAL BUG!!!:
        # i += 1
        # j += 1
        # while i > 0:
        #     while j > 0:
        #         res += self.tree[i][j]
        #         j -= j & (-j)
        #     i -= i & (-i)
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                res += self.tree[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return res



    def sumRegion(self, i1, j1, i2, j2):
        """
        :type i1: int
        :type j1: int
        :type i2: int
        :type j2: int
        :rtype: int
        """
        return self.getSum(i2, j2) - self.getSum(i1 - 1, j2) - self.getSum(i2, j1 - 1) + self.getSum(i1 - 1, j1 - 1)
