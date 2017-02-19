# Search a 2D Matrix

# Locate the row, then the column

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]:
            return False
        lo = 0
        hi = len(matrix) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if matrix[mid][-1] < target:
                lo = mid + 1
            elif matrix[mid][0] > target:
                hi = mid - 1
            else:
                break
        if lo > hi:
            return False
        row = matrix[mid]
        lo = 0
        hi = len(row) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if row[mid] < target:
                lo = mid + 1
            elif row[mid] > target:
                hi = mid - 1
            else:
                return True
        return False
