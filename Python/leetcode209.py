# Minimum Size Subarray Sum

# Two pointers from left to right. No need to sum up the list every time.

# Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.
#
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
#
# click to show more practice.
#
# More practice:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        start = 0
        end = 0
        res = 0
        subSum = nums[0]

        while end < length:
            if subSum < s:
                end += 1
                subSum += nums[end]
                if res != 0 and end - start >= res:
                    subSum -= nums[start]
                    start += 1
            else:
                if end == start:
                    return 1
                if res == 0 or end - start + 1 < res:
                    res = end - start + 1
                start = start += 1
        return res

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0: return 0
        start = 0
        end = 0
        res = 0
        subSum = nums[0]

        while True:
            while subSum < s:
                if end == length - 1:
                    return res
                end += 1
                subSum += nums[end]

            while subSum >= s:
                subSum -= nums[start]
                start += 1

            if res == 0 or res > end - start + 2:
                res = end - start + 2
        return res
