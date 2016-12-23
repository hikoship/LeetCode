# Top K Frequent Elements

# hash table 计数，反过来把次数排序

# Given a non-empty array of integers, return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        reverseCount = {}
        array = []
        for n in count:
            if count[n] in reverseCount:
                reverseCount[count[n]].append(n)
            else:
                reverseCount[count[n]] = [n]
                array.append(count[n])
        array.sort(reverse=True)
        res = []
        i = 0
        while k > 0:
            res += reverseCount[array[i]]
            k -= len(reverseCount[array[i]])
            i += 1
        return res
