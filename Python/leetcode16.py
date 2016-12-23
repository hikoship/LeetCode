# 3Sum Closest

# similar to 3Sum

# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        l = len(nums)
        res = nums[0] + nums[1] + nums[2]
        for i in range(l):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start = i + 1
            end = l - 1
            while start < end:
                if start > i + 1 and nums[start] == nums[start - 1]:
                    start += 1
                    continue
                if end < l - 1 and nums[end] == nums[end + 1]:
                    end -= 1
                    continue
                s = nums[i] + nums[start] + nums[end]
                if s == target:
                    return target
                elif s > target:
                    if s - target < abs(res - target):
                        res = s
                    end -= 1
                else:
                    if target - s < abs(res - target):
                        res = s
                    start += 1
        return res
