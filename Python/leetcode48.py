# Rotate Image

# first loop:
# xxxoxxx
# xxxoxxx
# xxxoxxx
# ooooooo
# xxxoxxx
# xxxoxxx
# xxxoxxx
# second loop:
# oooxooo
# oooxooo
# oooxooo
# xxxxxxx
# oooxooo
# oooxooo
# oooxooo
# oooxooo

# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Follow up:
# Could you do this in-place?

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for m in range(l / 2):
            for n in range(l / 2):
                tmp = matrix[m][n]
                matrix[m][n] = matrix[l - n - 1][m]
                matrix[l - n - 1][m] = matrix[l - m - 1][l - n - 1]
                matrix[l - m - 1][l - n - 1] = matrix[n][l - m - 1]
                matrix[n][l - m - 1] = tmp

        if l % 2:
            for i in range(l / 2):
                tmp = matrix[i][l / 2]
                matrix[i][l / 2] = matrix[l / 2][i]
                matrix[l / 2][i] = matrix[l - i - 1][l / 2]
                matrix[l - i - 1][l / 2] = matrix[l / 2][l - i - 1]
                matrix[l / 2][l - i - 1] = tmp

        return
