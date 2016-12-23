# Median of Two Sorted Arrays

# convert to getKth; get rid of half for each division.

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1), len2 = len(nums2)
        midl = (len1 + len2 + 1) / 2
        midr = (len1 + len2 + 2) / 2
        return self.getKth(nums1, nums2, 0, len1 - 1, 0, len2 - 1, midl)
            + self.getKth(num1, num2, 0, len1 - 1, 0, len2 - 1, midr)


    def getKth(self, nums1, nums2, l1, l2, r1, r2, k):
        if k == 1:
            if l1 > l2: return num2[0]
            elif r1 > r2: return num1[0]
            else: return min(num1[0], num2[0])
        if nums1[mid1] == nums2[mid2]:
            return nums1[mid1]
        if nums1[mid1] <
