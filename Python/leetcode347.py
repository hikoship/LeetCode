# Top K Frequent Elements

# hash table; sort using lambda

# Given a non-empty array of integers, return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# bucket sort
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        bucket = [[] for _ in range(len(nums))]
        for n in d:
            bucket[d[n] - 1].append(n)
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res += bucket[i]
        return res[:k]




# O(nlogn)
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        return sorted(d, key=lambda x: d[x], reverse=True)[:k]

# wtf is it..
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
