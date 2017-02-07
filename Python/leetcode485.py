# Max Consecutive Ones

# maxhere, maxall...

# Given a binary array, find the maximum number of consecutive 1s in this array.
#
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000

# good solution in discussion
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxHere, maxAll = 0, 0
        for n in nums:
            if n == 0:
                maxAll = max(maxAll, maxHere)
                maxHere = 0
            else:
                maxHere += 1
        return max(maxHere, maxAll)

# my awkward solution
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        prevOne = False
        start = len(nums)
        for i, n in enumerate(nums):
            if n == 0 and prevOne:
                res = max(res, i - start)
                prevOne = False
            if n == 1 and not prevOne:
                start = i
                prevOne = True
        if prevOne: # Wrong: forget this if clause
            res = max(res, len(nums) - start)
        return res
