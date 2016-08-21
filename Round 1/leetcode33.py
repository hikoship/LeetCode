# Search in Rotated Sorted Array

# Find the index of the least item first by comparing the middle element to the *right*most one.
# If comparing with the leftmost element, the algorithm fails on arrays like [1,2,3], where the least index is 0.

# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.

class Solution(object):
    def __init__(self):
        self.n = []
        self.t = 0
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.n = nums[:]
        self.t = target
        l = len(nums)
        leastItemIndex = self.getLeastItemIndex(0, l - 1)
        if target <= nums[-1]:
            return self.subSearch(leastItemIndex, l - 1)
        else:
            return self.subSearch(0, leastItemIndex - 1)


    def getLeastItemIndex(self, left, right):
        mid = (left + right) / 2
        if self.n[mid] > self.n[right]:
            left = mid + 1
        else:
            right = mid
        return self.getLeastItemIndex(left, right)

    def subSearch(self, left, right):
        if left > right:
            return -1
        mid = (left + right) / 2
        if self.n[mid] == self.t:
            return mid
        elif self.n[mid] < self.t:
            left = mid + 1
        else:
            right = mid - 1
        return self.subSearch(left, right)

# Iteration
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)

        # get the index of the least item
        left = 0
        right = l - 1
        while (left < right):
            mid = (left + right) / 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        leastItemIndex = left

        # find the target
        if target <= nums[l - 1]:
            left = leastItemIndex
            right = l - 1
        else:
            left = 0
            right = leastItemIndex - 1
        while (left <= right):
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
