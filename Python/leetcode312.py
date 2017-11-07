# Burst Balloons

# @dietpepsi: Be naive first, then identify what are *redundant* works
# for subarray [i, j], iterate the last balloon to burst, so that [i, last], [last, j] can be independent

# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
#
# Find the maximum coins you can collect by bursting the balloons wisely.
#
# Note:
# (1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# (2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
#
# Example:
#
# Given [3, 1, 5, 8]
#
# Return 167
#
#     nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#    coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = [1] + nums + [1]  # add start and end
        res = [[0] * (n + 2) for _ in range(n + 2)]
        for length in range(1, n + 1):
            # WRONG: for start in range(1, n + 1 - length):
            for start in range(1, n + 2 - length):
                end = start + length - 1
                for last in range(start, end + 1):
                    res[start][end] = max(res[start][end],
                                          res[start][last - 1] + res[last + 1][end] + nums[start - 1] * nums[last] *
                                          nums[end + 1])
        return res[1][n]
