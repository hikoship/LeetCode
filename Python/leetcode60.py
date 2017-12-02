# Permutation Sequence

# Math

# The set [1,2,3,…,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
#
# Note: Given n will be between 1 and 9 inclusive.

# Use Leetcode46: TLE
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = range(1, n + 1)
        return ''.join([str(i) for i in self.dfs(nums)[k - 1]])

    def dfs(self, nums):
        l = len(nums)
        if l == 1:
            return [[nums[0]]]
        perm = []
        for i in range(l):
            subPerm = self.dfs(nums[:i] + nums[i + 1:])
            for p in subPerm:
                perm.append([nums[i]] + p)
        return perm


# Math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = 0
        nums = range(1, n + 1)
        fac = [1]
        for i in range(1, 10):
            fac.append(i * fac[i - 1])

        while n > 0:
            i = (k - 1) / fac[n - 1]
            tmp = nums[i]
            res = 10 * res + tmp
            nums.remove(tmp)
            n -= 1
            k -= fac[n] * i
        return str(res)
