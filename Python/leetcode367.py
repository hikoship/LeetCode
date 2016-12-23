# Valid Perfect Square

# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
# Input: 16
# Returns: True
#
# Example 2:
#
# Input: 14
# Returns: False

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = 0
        r = 65536
        while l <= r:
            mid = (l + r) / 2
            if num == mid * mid:
                return True
            elif num < mid * mid:
                r = mid - 1
            else:
                l = mid + 1
        return False
