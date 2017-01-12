# Contains Duplicate II

# hashmap; index is increasing

# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i, v in enumerate(nums):
            if v in d and i - d[v] <= k:
                return True
            else:
                d[v] = i
        # for i in range(len(nums)):
        #     if nums[i] in d and i - d[nums[i]] <= k:
        #         return True
        #     else:
        #         d[nums[i]] = i
        #
        #     # Since i in increasing, there is no need to use abs and set.
        #     # if nums[i] in d:
        #     #     for idx in d[nums[i]]:
        #     #         if abs(idx - i) <= k:
        #     #             return True
        #     #     d[nums[i]].add(i)
        #     # else:
        #     #     # WRONG: d[nums[i]] = set()
        #     #     d[nums[i]] = set([i])
        return False
