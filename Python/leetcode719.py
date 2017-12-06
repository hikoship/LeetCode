# Find K-th Smallest Pair Distance

# list min and max distance, binary search, count pairs

# Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.
#
# Example 1:
# Input:
# nums = [1,3,1]
# k = 1
# Output: 0
# Explanation:
# Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
# Note:
# 2 <= len(nums) <= 10000.
# 0 <= nums[i] < 1000000.
# 1 <= k <= len(nums) * (len(nums) - 1) / 2.


class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        low = nums[1] - nums[0]
        for i in range(1, len(nums)):
            low = min(low, nums[i] - nums[i - 1])
        high = nums[-1] - nums[0]
        while low < high:
            mid = low + (high - low) / 2
            count = self.countPairs(nums, mid)
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low

    def countPairs(self, nums, maxVal):
        count = 0
        for i in range(len(nums)):
            low = i
            high = len(nums) - 1
            # last index j where n[j] - n[i] <= maxVal
            while low < high:
                mid = low + (high - low + 1) / 2
                if nums[mid] - nums[i] <= maxVal:
                    low = mid
                else:
                    high = mid - 1
            count += low - i
        return count
