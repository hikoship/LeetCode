# Two Sum

#

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# UPDATE (2016/2/13):
# The return format had been changed to zero-based indices. Please read the above updated description carefully.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        sortedNums = nums[:]
        sortedNums.sort()
        a = 0
        b = l - 1
        while a <= b:
            va = sortedNums[a]
            vb = sortedNums[b]
            if  va + vb == target:
                x = nums.index(va)
                if va == vb:
                    y = nums[x + 1:].index(vb) + x + 1
                else:
                    y = nums.index(vb)
                return [x, y]
            elif va + vb < target:
                a += 1
            else:
                b -= 1
        return
