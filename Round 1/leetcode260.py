# LeetCode 260
# Single Number III

# 把题目拆成两个 single I 来做，分组。分组原则是两个结果不在同一组中，所以判断他们第一个不同的位在哪里。根据这个位上的数值来分组。

# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
#
# For example:
#
# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
#
# Note:
# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xorRes = 0
        for num in nums:
            xorRes ^= num
        lowestDiff = xorRes & ~(xorRes - 1) # only that bit is set
        x = 0
        y = 0
        for num in nums:
            if num & lowestDiff:
                x ^= num
            else:
                y ^= num
        return [x, y]
            
