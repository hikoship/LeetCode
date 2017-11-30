# 3Sum Closest

# similar to 3Sum

# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# using k-sum
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        return self.kSum(nums, 3, 0, target)


    def kSum(self, nums, k, start, target):
        if k == 2:
            return self.twoSum(nums, start, target)
        res = float('inf')
        i = start
        while i < len(nums):
            # WRONG: for subArr in self.kSum(nums, k - 1, i, target - nums[i]):
            tmp = self.kSum(nums, k - 1, i + 1, target - nums[i]) + nums[i]
            if tmp == target:
                return tmp
            if abs(tmp - target) < abs(res - target):
                res = tmp
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        return res


    def twoSum(self, nums, start, target):
        res = float('inf')
        s = set()
        i = start
        j = len(nums) - 1
        while i < j:
            tmp = nums[i] + nums[j]
            if tmp == target:
                return target
            if abs(tmp - target) < abs(res - target):
                res = tmp
            if tmp < target:
                i += 1
            else:
                j -= 1
        return res



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
