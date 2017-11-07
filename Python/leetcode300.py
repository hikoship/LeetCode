# Longest Increasing Subsequence

# Thanks to Sam Fu.
# or binary search: the array records smallest tails of sequences of length i

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


# DP O(n^2)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Denote length(i) as the length of LIS ending with ai.
        # Denote prev(i) as the previous index of ai in the LIS.
        # Denote max as the index of the last element of LIS.
        if nums == []:
            return 0
        n = len(nums)
        length = [1] * n
        prev = [-1] * n
        maxIndex = 0

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and length[i] < length[j] + 1:
                    length[i] = length[j] + 1
                    prev[i] = j
                    if length[i] > length[maxIndex]:
                        maxIndex = i
        return length[maxIndex]

        # if you wan to return the content of LIS:
        # result = []
        # i = maxIndex
        # print length[maxIndex]
        # while prev[i] != -1:
        #     result.append(a[i])
        #     i = prev[i]
        # result.append(a[i])
        # return result[::-1]

# binary search: O(nlogn)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for x in nums:
            if len(res) == 0 or x > res[-1]:
                res.append(x)
            else:
                left = 0
                right = len(res) - 1
                while left < right:
                    mid = (left + right) / 2
                    if x <= res[mid]:
                        right = mid
                    else:
                        left = mid + 1
                res[left] = x
        return len(res)
