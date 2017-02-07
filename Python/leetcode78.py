# Subsets

# use combinations..
# update: to appear or not to appear

# Given a set of distinct integers, nums, return all possible subsets.
#
# Note: The solution set must not contain duplicate subsets.
#
# For example,
# If nums = [1,2,3], a solution is:
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        def f(i):
            if i == len(nums):
                return
            f(i + 1)
            # Wrong: res will grow forever
            # for x in res:
            #     res.append([nums[i]] + res)
            for j in range(len(res)):
                res.append([nums[i]] + res[j])
        f(0)
        return res

# what the hell is this...
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        res = [[], nums]
        for i in range(1, l):
            comb = self.genComb(l, i)
            for case in comb:
                subset = []
                for digit in case:
                    subset.append(nums[digit - 1])
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
