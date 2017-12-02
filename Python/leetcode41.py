# First Missing Positive

# tricky: while 0 < nums[i] <= N and nums[nums[i] - 1] != nums[i]:

# Given an unsorted integer array, find the first missing positive integer.
#
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
# Your algorithm should run in O(n) time and uses constant space.
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        for i in range(N):
            # BUG: very tricky... while 0 < nums[i] <= N and i + 1 != nums[i]:
            while 0 < nums[i] <= N and nums[nums[i] - 1] != nums[i]:
                tmp = nums[i]
                nums[i] = nums[tmp - 1]
                nums[tmp - 1] = tmp

        for i in range(N):
            if nums[i] != i + 1:
                return i + 1
        return N + 1
