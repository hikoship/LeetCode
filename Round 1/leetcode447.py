# Number of Boomerangs

# use a dict to map distance and number of nodes for every node.
# but do not really store distance... store its square.

# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
# 
# Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
# 
# Example:
# Input:
# [[0,0],[1,0],[2,0]]
# 
# Output:
# 2
# 
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p1 in points:
            d = {}
            for p2 in points:
                dis = self.f(p1, p2)
                if dis in d:
                    d[dis] += 1
                else:
                    d[dis] = 1
            for v in d.values():
                res += v * (v - 1) # 2Pv
        return res
        
    def f(self, p1, p2):
        x = abs(p1[0] - p2[0])
        y = abs(p1[1] - p2[1])
        return x * x + y * y
