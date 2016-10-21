class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                # sort remaining subarray
                # Note! nums = nums[:i] + sorted(nums[i:]) cannot get correct answer because it allocates a new piece of memory to nums, and the original value doesn't change.
                nums[i:] = sorted(nums[i:])
                j = i
                while nums[j] <= nums[i - 1]: # <= instead of < in order to handle arrays like [1,1,5]
                    j += 1
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                return
            i -= 1
        nums.reverse()
