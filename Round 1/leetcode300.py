# Longest Increasing Subsequence

# Thanks to Sam Fu.

# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.
#
# Your algorithm should run in O(n2) complexity.
#
# Follow up: Could you improve it to O(n log n) time complexity?
#
# Credits:
# Special thanks to @pbrother for adding this problem and creating all test cases.

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        res = []
        for e in nums:
            if len(res) > 0 and e > res[-1]:
                res.append(e)
                continue
            left = 0
            right = len(res) - 1
            while (left < right):
                mid = (left + right) / 2
                if e == res[mid]:
                    left = mid
                    break
                elif e < res[mid]:
                    right = mid
                else:
                    left = mid + 1
            res[left] = e
        return len(res)
