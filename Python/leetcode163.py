# Missing Ranges

# be careful with empty nums

# Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
#
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if len(nums) == 0:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + "->" + str(upper)]
        prev = lower - 1
        res = []
        for n in nums:
            if n == prev + 2:
                res.append(str(prev + 1))
            elif n > prev + 2:
                res.append(str(prev + 1) + "->" + str(n - 1))
            prev = n
        if nums[-1] == upper - 1:
            res.append(str(upper))
        elif nums[-1] < upper - 1:
            res.append(str(n + 1) + "->" + str(upper))
        return res
