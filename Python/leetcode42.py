class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(height) - 1
        while lo <= hi:
            
