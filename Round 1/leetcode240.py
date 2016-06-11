# Search a 2D Matrix II

# first thought: divide conquer. Split the matrix to a half and a quarter.
# second thought: search from the bottom-left or top-right corner.

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
#
# Given target = 20, return false.

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])
        i = row - 1
        j = 0
        while i >= 0 and j < col:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
        return False



class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        if row == 0:
            return False
        col = len(matrix[0])
        if col == 0:
            return False
        midRow = row / 2
        midCol = col / 2
        if matrix[midRow][midCol] == target:
            return True
        elif matrix[midRow][midCol] < target:
            if self.searchMatrix(matrix[midRow + 1:], target): # bottom
                return True
            elif self.searchMatrix([r[midCol + 1:] for r in matrix[:midRow + 1]], target): #top-right
                return True
            else:
                return False
        else:
            if self.searchMatrix(matrix[:midRow], target): # top
                return True
            elif self.searchMatrix([r[:midCol] for r in matrix[midRow:]], target): #bottom-left
                return True
            else:
                return False
