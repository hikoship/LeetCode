# Permutations II

# sort and jump over duplicated items

# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
# 
# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return []
        res = []
        nums.sort()
        self.dfs(res, nums, [])
        return res

    def dfs(self, res, nums, prev):
        l = len(nums)
        if l == 0:
            res.append(prev)
        for i in range(l):
            if i == 0 or nums[i - 1] < nums[i]:
                subPerm = self.dfs(res, nums[:i] + nums[i + 1:], prev + [nums[i]])
