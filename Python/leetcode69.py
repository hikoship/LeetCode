# Sqrt(x)

# 两边逼近

# Implement int sqrt(int x).
#
# Compute and return the square root of x.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        minrt = 0
        maxrt = x
        while maxrt - minrt > 1:
            mid = (maxrt + minrt) / 2
            mid2 = mid * mid
            if mid2 == x:
                return mid
            elif mid2 < x:
                minrt = mid
            else:
                maxrt = mid

        return maxrt if maxrt * maxrt == x else minrt
