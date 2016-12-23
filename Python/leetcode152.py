# Maximum Product Subarray

# record both max and min

# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
# 
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        tmpRes = res
        tmpMin = res
        for i in range(1, len(nums)):
            tmpRes, tmpMin = max(nums[i], nums[i] * tmpRes, nums[i] * tmpMin), min(nums[i], nums[i] * tmpRes, nums[i] * tmpMin)
            res = max(res, tmpRes)
        return res