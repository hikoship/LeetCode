# Reshape the Matrix

# easy

# In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.
#
# You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.
#
# The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.
#
# If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
#
# Example 1:
# Input:
# nums =
# [[1,2],
#  [3,4]]
# r = 1, c = 4
# Output:
# [[1,2,3,4]]
# Explanation:
# The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
# Example 2:
# Input:
# nums =
# [[1,2],
#  [3,4]]
# r = 2, c = 4
# Output:
# [[1,2],
#  [3,4]]
# Explanation:
# There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
# Note:
# The height and width of the given matrix is in range [1, 100].
# The given r and c are all positive.

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        oldRow = len(nums)
        oldCol= len(nums[0]) # height and width are in [1, 100]
        if oldRow * oldCol != r * c:
            return nums
        newMat = [[0] * c for _ in range(r)]
        i = 0
        j = 0
        x = 0
        y = 0
        while x < r and y < c:
            newMat[x][y] = nums[i][j]
            y += 1
            if y == c:
                x += 1
                y = 0
            j += 1
            if j == oldCol:
                i += 1
                j = 0
        return newMat

# slow
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        allNums = reduce(lambda x, y: x + y, nums)
        if len(allNums) != r * c:
            return nums
        newMat = []
        for i in range(r):
            newMat.append(allNums[i * c : i * c + c])
        return newMat
