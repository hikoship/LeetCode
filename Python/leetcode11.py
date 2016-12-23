# container with most water

# find the bucket from two ends to middle. The pointer with lower height can be safely moved because the potential maximum result must have a higher height since the width decreases.

# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        res = 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            elif height[i] > height[j]:
                res = max(res, height[j] * (j - i))
                j -= 1
            else:
                res = max(res, height[i] * (j - i))
                i += 1
                j -= 1
        return res
