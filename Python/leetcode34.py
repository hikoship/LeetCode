# Search for a Range

# divide conquer. let the right index be len(n) - 1, instead of len(n). Note how to calculate middle.

# Given a sorted array of integers, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        head = -1
        tail = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                head = self.searchLeft(nums, target, left, mid)
                tail = self.searchRight(nums, target, mid, right)
                break
        return [head, tail]

    def searchLeft(self, nums, target, left, right):
        while left < right:
            mid = (left + right) / 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def searchRight(self, nums, target, left, right):
        while left < right:
            mid = (left + right + 1) / 2 # Note! plus one
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        return left
