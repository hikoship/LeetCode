# Subsets II

# sort first

# Given a collection of integers that might contain duplicates, nums, return all possible subsets.
#
# Note: The solution set must not contain duplicate subsets.
#
# For example,
# If nums = [1,2,2], a solution is:
#
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(res, nums, [], 0)
        return res

    def dfs(self, res, nums, prev, start):
        res.append(list(prev))
        for i in range(start, len(nums)):
            if i == start or nums[i] > nums[i - 1]:
                prev.append(nums[i])
                self.dfs(res, nums, prev, i + 1)
                prev.pop()

# Similar to #78. sort first. query before insert.
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l = len(nums)
        res = [[], nums]
        for i in range(1, l):
            comb = self.genComb(l, i)
            for case in comb:
                subset = []
                for digit in case:
                    subset.append(nums[digit - 1])
                if not subset in res:
                    res.append(subset)
        return res

    def genComb(self, n, k):
        a = range(1, k + 1)
        res = []
        while True:
            cur = k - 1
            while a[cur] <= n:
                res.append(a[:])
                a[cur] += 1
            while a[cur] > n - k + cur:
                cur -= 1
                if cur < 0:
                    return res
            a[cur] += 1
            for i in range(cur + 1, k):
                a[i] = a[cur] + i - cur
