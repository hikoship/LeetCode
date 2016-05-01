# Set Matrix Zeroes

#

# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
#
# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        flag = False
        col = []
        for r in range(m):
            flag = False
            for c in range(n):
                if matrix[r][c] == 0:
                    flag = True
                    if not c in col:
                        col.append(c)
            if flag:
                matrix[r] = [0] * n

        for r in range(m):
            for c in col:
                matrix[r][c] = 0

        return
