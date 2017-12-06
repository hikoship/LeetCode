# Find K Pairs with Smallest Sums

# heap, push (0, j) first. klogk

# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
#
# Define a pair (u,v) which consists of one element from the first array and one element from the second array.
#
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
#
# Example 1:
# Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3
#
# Return: [1,2],[1,4],[1,6]
#
# The first 3 pairs are returned from the sequence:
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# Example 2:
# Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2
#
# Return: [1,1],[1,1]
#
# The first 2 pairs are returned from the sequence:
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# Example 3:
# Given nums1 = [1,2], nums2 = [3],  k = 3
#
# Return: [1,3],[2,3]
#
# All possible pairs are returned from the sequence:
# [1,3],[2,3]


# only push (0, 0) first, intuitive
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        if nums1 == [] or nums2 == []:
            return []
        heapq.heappush(heap, [nums1[0] + nums2[0], 0, 0])
        res = []
        visited = [[False] * len(nums2) for _ in range(len(nums1))]
        while len(res) < k and heap:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if i < len(nums1) - 1 and not visited[i + 1][j]:
                visited[i + 1][j] = True
                heapq.heappush(heap, [nums1[i + 1] + nums2[j], i + 1, j])
            if j < len(nums2) - 1 and not visited[i][j + 1]:
                visited[i][j + 1] = True
                heapq.heappush(heap, [nums1[i] + nums2[j + 1], i, j + 1])
        return res



# push (0, j) first, no visited
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        if nums1 == [] or nums2 == []:
            return []
        for i in range(len(nums1)):
            if i == k:
                break
            heapq.heappush(heap, [nums1[i] + nums2[0], i, 0])
        res = []
        while len(res) < k and heap:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            j += 1
            if j < len(nums2):
                heapq.heappush(heap, [nums1[i] + nums2[j], i, j])
        return res

# Wrong
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        res = []
        while len(res) < k and i < len(nums1) and j < len(nums2):
            res.append([nums1[i], nums2[j]])
            if i == len(nums1) - 1:
                j += 1
            elif j == len(nums2) - 1:
                i += 1
            elif nums1[i] + nums2[j + 1] < nums1[i + 1] + nums2[j]:
                j += 1
            else:
                i += 1
        return res
