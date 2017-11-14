# Jump Game II

# For each step, iterate from current index to the farthest index,
# then get the next farthest index we can reach in next step.

# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# For example:
# Given array A = [2,3,1,1,4]
#
# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
#
# Note:
# You can assume that you can always reach the last index.

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        i = 0
        curMax = 0
        nextMax = 0
        res = 1
        while True:
            while i <= curMax:
                nextMax = max(nextMax, i + nums[i])
                if nextMax >= len(nums) - 1:
                    return res
                i += 1
            curMax = nextMax
            res += 1
