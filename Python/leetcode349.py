# Intersection of Two Arrays

#

# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
#
# Note:
# Each element in the result must be unique.
# The result can be in any order.

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = set()
        s = set()
        for n in nums1:
            s.add(n)
        for n in nums2:
            if n in s:
                res.add(n)
        return list(res)

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                tmp = nums1[i]
                res.append(tmp)
                while i < len(nums1) and nums1[i] == tmp:
                    i += 1
                while j < len(nums2) and nums2[j] == tmp:
                    j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res
