# 3Sum

# TLE if using the method in Subset II. Princeton Algorithm I: sort and binary search

# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note: The solution set must not contain duplicate triplets.
#
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# sort and two pointers
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l = len(nums)
        res = []
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
                if s == 0:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                elif s > 0:
                    end -= 1
                else:
                    start += 1
        return res



# sort and binary search
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        res = []
        for i in range(length):
            if i == 0 or nums[i] != nums[i - 1]:
                for j in range(i + 1, length):
                    if j == i + 1 or  nums[j] != nums[j - 1]:
                        if -(nums[i] + nums[j]) in nums[j + 1:]:
                            res.append([nums[i], nums[j], -(nums[i] + nums[j])])
        return res

# !TLE
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l = len(nums)
        res = []
        comb = self.genComb(l, 3)
        for case in comb:
            subset = []
            for digit in case:
                subset.append(nums[digit - 1])
            if sum(subset) == 0 and not subset in res:
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
