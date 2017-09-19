# WRONG solution (fail to pass [4,5,5,6])
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums)
        i = 0
        j = 0
        while i < len(nums):
            nums[i] = arr[j]
            i += 2
            j += 1
        i = 1
        while i < len(nums):
            nums[i] = arr[j]
            i += 2
            j += 1
