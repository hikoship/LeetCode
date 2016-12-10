# 4Sum

# 1. sort
# 2. for NSum with target t, do (N-1)Sum with target t - xi for every xi
# 3. use two pointers to solve 2Sum

# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# 
# Note: The solution set must not contain duplicate quadruplets.
# 
# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.NSum(nums, target, res, 4, [])
        return res

    def NSum(self, nums, target, res, N, prev):
        if N < 2:
            return
        if N == 2:
            # two sum
            l = 0
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append(prev + [nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1 
        else:
            # reduce NSum to (N-1)Sum
            for i in range(len(nums) - N + 1):
                if N * nums[i] > target or N * nums[-1] < target:
                    break
                if i == 0 or nums[i] != nums[i - 1]:
                    # remove duplicates
                    self.NSum(nums[i + 1:], target - nums[i], res, N - 1, prev + [nums[i]])
