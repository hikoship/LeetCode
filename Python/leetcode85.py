# Maximal Rectangle

# Use largest histogram solution in lc84

# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#
# For example, given the following matrix:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 6.

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        res = 0
        heights = [0] * len(matrix[0])
        for line in matrix:
            for i in range(len(heights)):
                if line[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
            res = max(res, self.helper(heights))
        return res



    # from LC84
    def helper(self, heights):
        heights.append(0)
        stack = [-1]
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                # WRONG: h = stack.pop()
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        heights.pop()
        return res
