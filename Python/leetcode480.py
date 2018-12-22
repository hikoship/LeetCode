class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        for i in range(len(nums) - k + 1):
            subArray = nums[i : i + k]
            heapq.heapify(subArray)
