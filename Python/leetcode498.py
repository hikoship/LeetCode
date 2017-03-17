# Diagonal Traverse

# move current point

# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
#
# Example:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output:  [1,2,4,7,5,3,6,8,9]
#
# Note:
# The total number of elements of the given matrix will not exceed 10,000.

# fast solution by @shawngao: loop based on movement
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        res = []
        M = len(matrix)
        N = len(matrix[0])
        r = 0
        c = 0
        while True:
            res.append(matrix[r][c])
            if r == M - 1 and c == N - 1:
                return res
            if (r + c) % 2 == 0:
                # upright
                if c == N - 1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:
                if r == M - 1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1


# my slow solution: loop based on line
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        res = []
        M = len(matrix)
        N = len(matrix[0])
        for i in range(M + N - 1):
            if i % 2 == 0:
                if i < M:
                    r = i
                    c = 0
                else:
                    # WRONG: r = M
                    r = M - 1
                    c = i - M + 1
                while r >= 0 and c < N:
                    res.append(matrix[r][c])
                    r -= 1
                    c += 1
            else:
                if i < N:
                    r = 0
                    c = i
                else:
                    r = i - N + 1
                    # WRONG: c = N
                    c = N - 1
                while r < M and c >= 0:
                    res.append(matrix[r][c])
                    r += 1
                    c -= 1
        return res
