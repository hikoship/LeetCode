# Majority Element

# voting algorithm

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = 0
        count = 0
        for n in nums:
            if n == candidate:
                count += 1
            elif count == 0:
                candidate = n
                count = 1
            else:
                count -= 1
        return candidate


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) / 2]
