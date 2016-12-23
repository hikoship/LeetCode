# Combination Sum

# sort and use start index

# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7,
# A solution set is:
# [
#   [7],
#   [2, 2, 3]
# ]

class Solution(object):
    def combinationSum(self, candidates, target):
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
            # i > 0 is also correct, but for #40, only i > start works.
            if i > start and x == candidates[i - 1]:
                continue
            if x > target:
                return res
            if x == target:
                res.append([x])
                return res
            tmp = self.f(candidates, target - x, i)
            for y in tmp:
                res.append([x] + y)

        return res
