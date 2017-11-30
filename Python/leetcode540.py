# Single Element in a Sorted Array

# binary search easy

# Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.
#
# Example 1:
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10
# Note: Your solution should run in O(log n) time and O(1) space.




class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if (mid == 0 or nums[mid] != nums[mid - 1] ) and (mid == len(nums) - 1 or nums[mid] != nums[mid + 1]):
                return nums[mid]
            if mid % 2 and nums[mid] == nums[mid - 1] or mid % 2 == 0 and mid < len(nums) and nums[mid] == nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]
