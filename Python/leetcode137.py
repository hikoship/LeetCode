# Single Number II

# Python 对 32 位有限制；将每个位的出现次数累加起来。

# Given an array of integers, every element appears three times except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask = 1
        res = 0
        for i in range(32):
            cnt = 0
            for n in nums:
                if mask & n:
                    cnt += 1
            if cnt % 3:
                res |= mask
            mask = mask << 1
        # post process for Python
        if res > 2147483647:
            res = -(4294967295 ^ res) - 1
        return res
