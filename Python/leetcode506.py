# Relative Ranks

# sort

# Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".
#
# Example 1:
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
# For the left two athletes, you just need to output their relative ranks according to their scores.
# Note:
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        a = [[e, i] for i, e in enumerate(nums)]
        a.sort(reverse = True)
        res = [''] * len(nums)
        # don't forget 'if'
        if len(nums) > 0:
            res[a[0][1]] = 'Gold Medal'
        if len(nums) > 1:
            res[a[1][1]] = 'Silver Medal'
        if len(nums) > 2:
            res[a[2][1]] = 'Bronze Medal'
        for i in range(3, len(a)):
            res[a[i][1]] = str(i + 1)
        return res
