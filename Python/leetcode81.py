# Search in Rotated Sorted Array II

#

# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
#
# Would this affect the run-time complexity? How and why?
#
# Write a function to determine if a given target is in the array.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = len(nums)
        left = 0
        right = l - 1
        while (left <= right):
            print left,right
            mid = (left + right) / 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] < nums[right]: # right side is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else: # left side is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False
