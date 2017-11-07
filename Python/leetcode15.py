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


# concise kSum
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.kSum(nums, 3, 0, 0)


    def kSum(self, nums, k, start, target):
        if k == 2:
            return self.twoSum(nums, start, target)
        res = []
        i = start
        while i < len(nums):
            # WRONG: for subArr in self.kSum(nums, k - 1, i, target - nums[i]):
            for subArr in self.kSum(nums, k - 1, i + 1, target - nums[i]):
                res.append([nums[i]] + subArr)
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        return res


    def twoSum(self, nums, start, target):
        res = []
        s = set()
        i = start
        while i < len(nums):
            # WRONG: if nums[i] in s:
            if target - nums[i] in s:
                res.append([target - nums[i], nums[i]])
                i += 1
                while i < len(nums) and nums[i] == nums[i - 1]:
                    i += 1
            else:
                s.add(nums[i])
                i += 1
        return res



class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        visited = [False] * len(nums)
        self.NSum(nums, 0, visited, 0, 3, res, [])
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

# WTF???
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
