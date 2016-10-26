# House Robber II

# Run twice: one without head and one without tail

# Note: This is an extension of House Robber.
#
# After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        return max(self.f(nums[1:]), self.f(nums[:-1]))

    def f(self, nums):
        l = len(nums)
        if l == 0:
            return 0
        if l < 3:
            return max(nums)
        m = [nums[0], max(nums[0], nums[1])]
        for i in range(2, l):
            m.append(max(m[i - 1], m[i - 2] + nums[i]))
        return m[-1]

# tricky: pass index instead of array
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        if l < 4:
            return max(nums)
        return max(self.f(nums, l, 1), self.f(nums,l, 0))

    def f(self, nums, l, noHead):
        m = [nums[noHead], max(nums[noHead], nums[noHead + 1])]
        for i in range(noHead + 2, noHead + l - 1):
            m.append(max(m[i - noHead - 1], m[i - noHead - 2] + nums[i]))

        return m[-1]
