# House Robber

# DP

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# O(n) + O(1) @tusizi
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prevNo = 0
        prevYes = 0
        for n in nums:
            temp = prevNo
            prevNo = max(prevNo, prevYes)
            prevYes = temp + n
        return max(prevNo, prevYes)


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        if l < 3:
            return max(nums)
        m = [nums[0], max(nums[0], nums[1])]
        for i in range(2, l):
            m.append(max(m[i - 1], m[i - 2] + nums[i]))
        return m[-1]
