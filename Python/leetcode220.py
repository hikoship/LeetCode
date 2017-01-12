# Contains Duplicate III

# Note that we don't need to store all nums into buckets.
# Actually each bucket contains only one element.
# If there has already been a number in the bucket, just return true.
# To avoid the condition that the difference of the two numbers in the same bucket is larger than k, we remove elements whose indices are more than k less than the current index.

# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 0 or t < 0: # WRONG: don't forget that
            return False
        bucketsDict = {}
        for i, n in enumerate(nums):
            # WRONG: put this part before if n > 0...
            if i > k:
                if nums[i - k - 1] >= 0:
                    bucket = nums[i - k - 1] / (t + 1)
                else:
                    bucket = -((-nums[i - k - 1] - 1) / (t + 1)) - 1
                if bucket in bucketsDict:
                    del bucketsDict[bucket]
            if n >= 0:
                # WRONG: bucket = n / t
                bucket = n / (t + 1)
            else:
                # WRONG: bucket = -((-n - 1) / (t + 1))
                bucket = -((-n - 1) / (t + 1)) - 1
            if bucket in bucketsDict or (bucket - 1 in bucketsDict and n - bucketsDict[bucket - 1] <= t) or (bucket + 1 in bucketsDict and bucketsDict[bucket + 1] - n <= t):
                return True
            bucketsDict[bucket] = n

        return False
