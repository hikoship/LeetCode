# Spiral Matrix

# rowBeg, rowEnd, colBeg, colEnd...

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# For example,
# Given the following matrix:
#
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        res = []
        rowBeg = 0
        rowEnd = len(matrix) - 1
        colBeg = 0
        colEnd = len(matrix[0]) - 1
        while rowBeg < rowEnd and colBeg < colEnd:
            for j in range(colBeg, colEnd):
                res.append(matrix[rowBeg][j])
            for i in range(rowBeg, rowEnd):
                res.append(matrix[i][colEnd])
            for j in range(colEnd, colBeg, -1):
                res.append(matrix[rowEnd][j])
            for i in range(rowEnd, rowBeg, -1):
                res.append(matrix[i][colBeg])
            rowBeg += 1
            rowEnd -= 1
            colBeg += 1
            colEnd -= 1
        if rowBeg == rowEnd:
            for j in range(colBeg, colEnd + 1):
                res.append(matrix[rowBeg][j])
        # BUG: else:
        elif colBeg == colEnd:
            for i in range(rowBeg, rowEnd + 1):
                res.append(matrix[i][colBeg])
        return res
