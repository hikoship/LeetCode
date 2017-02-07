# Hamming Distance

# xor (no need use a mask)

# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.

# a good solution in discussion
class Solution(object):
    def hammingDistance(self, x, y):
        xor = x ^ y
        res = 0
        for i in range(32):
            res += (xor >> i) & 1
        return res

# my awkward one
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        mask = 1
        xor = x ^ y
        res = 0
        for i in range(32):
            if xor & (mask << i):
                res += 1
        return res
