# Sliding Window Maximum

# monotonic queue

# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
#
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Therefore, return the max sliding window as [3,3,5,5,6,7].
#
# Note:
# You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.
#
# Follow up:
# Could you solve it in linear time?


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums == []:
            return []
        deq = collections.deque()
        for i in range(k):
            while len(deq) > 0 and nums[i] >= nums[deq[-1]]:
                deq.pop()
            deq.append(i)
        res = [nums[deq[0]]]
        for i in range(k, len(nums)):
            if i - deq[0] >= k:
                deq.popleft()
            while len(deq) > 0 and nums[i] >= nums[deq[-1]]:
                deq.pop()
            deq.append(i)
            res.append(nums[deq[0]])
        return res
