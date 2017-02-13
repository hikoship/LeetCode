# Combination Sum II

# similar to #39

# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(res, candidates, target, [], 0)
        return res

    def dfs(self, res, candidates, target, prev, start):
        if target == 0:
            res.append(list(prev))
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            if i == start or candidates[i] > candidates[i - 1]:
                prev.append(candidates[i])
                self.dfs(res, candidates, target - candidates[i], prev, i + 1)
                prev.pop()


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.f(candidates, target, 0)

    def f(self, candidates, target, start):
        res = []
        for i in range(start, len(candidates)):
            x = candidates[i]
            if i > start and x == candidates[i - 1]:
                continue
            if x > target:
                return res
            if x == target:
                res.append([x])
                return res
            tmp = self.f(candidates, target - x, i + 1) # only change compared to #39
            for y in tmp:
                res.append([x] + y)

        return res
