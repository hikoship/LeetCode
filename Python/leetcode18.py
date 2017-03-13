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
        visited = [False] * len(nums)
        self.NSum(nums, 0, visited, target, 4, res, [])
        return res

    def NSum(self, nums, start, visited, target, N, res, prev):
        if N < 2 or N > len(nums):
            return
        if N == 2:
            # two sum
            s = set()
            dup = set()
            for i in range(start, len(nums)):
                if target - nums[i] in s and not nums[i] in dup:
                    res.append(prev + [target - nums[i], nums[i]])
                    dup.add(nums[i])
                else:
                    s.add(nums[i])
        else:
            # reduce NSum to (N-1)Sum
            for i in range(start, len(nums)):
                if N * nums[i] > target or N * nums[-1] < target:
                    break
                if not visited[i] and (i == 0 or nums[i] != nums[i - 1] or visited[i - 1]):
                    # remove duplicates
                    visited[i] = True
                    self.NSum(nums, i + 1, visited, target - nums[i], N - 1, res, prev + [nums[i]])
                    visited[i] = False
