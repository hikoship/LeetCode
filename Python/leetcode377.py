# Combination Sum IV

# Use DP to avoid exponential complexity

# Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
#
# Example:
#
# nums = [1, 2, 3]
# target = 4
#
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
#
# Note that different sequences are counted as different combinations.
#
# Therefore the output is 7.
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?

# TLE
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= 0:
            return 0
        res = 0
        for x in nums:
            if x == target:
                res += 1
            res += self.combinationSum4(nums, target - x)
        return res

# DP
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        store = [-1] * (target + 1)
        return self.f(nums, target, store)

    def f(self, nums, target, store):
        if target <= 0:
            return 0
        if store[target] >= 0:
            return store[target]

        res = 0
        for x in nums:
            if x == target:
                res += 1
            res += self.f(nums, target - x, store)
        store[target] = res
        return res
