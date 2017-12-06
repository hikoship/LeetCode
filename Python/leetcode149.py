# Max Points on a Line

# create map for each point, calculate local max. do not create map for each line.

# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        N = len(points)
        res = 0
        for i in range(N):
            localMax = 0
            coeff = {} # map line to points
            samePoint = 1
            for j in range(i + 1, N):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    samePoint += 1
                else:
                    tmp = self.getCoeff(points[i], points[j])
                    if tmp not in coeff:
                        coeff[tmp] = 0
                    coeff[tmp] += 1
                    localMax = max(localMax, coeff[tmp])
            res = max(res, localMax + samePoint)
        return res

    def getCoeff(self, p, q):
        a = q.x - p.x
        b = q.y - p.y
        if a == 0:
            return (1, 0)
        if b == 0:
            return (0, 1)
        gcd = self.getGcd(a, b)
        return (b / gcd, a / gcd)

    def getGcd(self, a, b):
        if b == 0:
            return a
        return self.getGcd(b, a % b)




# WRONG
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        N = len(points)
        if N <= 2:
            return N
        lines = {} # map line to points
        res = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                line = self.getLine(points[i], points[j])
                if line not in lines:
                    lines[line] = set()
                lines[line].add(i)
                lines[line].add(j)
                res = max(res, len(lines[line]))
        return res

    def getLine(self, p, q):
        # (x - p.x) * (q.y - p.y) = (y - p.y) * (q.x - p.x)
        # (q.y - p.y) * x - (q.x - p.x) * y + p.y * (q.x - p.x) - p.x * (q.y - p.y)
        p
        coeffX = q.y - p.y
        coeffY = q.x - p.x
        b = p.y * (q.x - p.x) - p.x * (q.y - p.y)
        if coeffX != 0:
            coeffY = float(coeffY) / coeffX
            b = float(b) / coeffX
            coeffX = 1
        elif coeffY != 0:
            b = float(b) / coeffY
            coeffY = 1
        else:
            b = 0
        return (coeffX, coeffY, b)
