# Maximum Subarray

# DP

# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
#
# click to show more practice.
#
# More practice:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = list(nums)
        for i in range(1, len(nums)):
            if sums[i - 1] > 0:
                sums[i] += sums[i - 1]
        return max(sums)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxAll = nums[0]
        maxHere = 0
        for n in nums:
            maxHere = max(maxHere + n, n)
            maxAll = max(maxHere, maxAll)
        return maxAll
