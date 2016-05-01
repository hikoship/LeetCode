# LeetCode 228
# Summary Ranges

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        l = len(nums)
        strlist = []
        i = 0

        while i < l:
            x = nums[i]
            s = str(x)
            i += 1
            if i < l and nums[i] - x == 1:
                while i < l and nums[i] - x == 1:
                    # in serial
                    x = nums[i]
                    i += 1
                s += '->' + str(x)

            strlist.append(s)

        return strlist
