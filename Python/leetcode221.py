# Maximal Square

# Store the max square ending with [i][j], not the max square within [i][j]

# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
# For example, given the following matrix:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 4.

# O(n^2) space complexity
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res = 0
        maxHere = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    maxHere[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == '0':
                        maxHere[i][j] = 0
                    else:
                        maxHere[i][j] = min(maxHere[i - 1][j - 1], maxHere[i][j - 1], maxHere[i - 1][j]) + 1
                res = max(res, maxHere[i][j])
        return res * res

# O(n) space complexity
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        res = 0
        tmp = 0
        maxHere = [0 for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(maxHere)):
                # use prev and tmp to store [i - 1][j - 1] and [i - 1][j]
                # Note: the location to put them
                prev = tmp
                tmp = maxHere[j]
                if j == 0:
                    maxHere[j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == '0':
                        maxHere[j] = 0
                    else:
                        maxHere[j] = min(prev, maxHere[j - 1], tmp) + 1
                res = max(res, maxHere[j])
        return res * res
