# Median of Two Sorted Arrays

# stretch N to 2 * N + 1
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

# stretch
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        N1 = len(nums1)
        N2 = len(nums2)
        if N1 < N2:
            return self.findMedianSortedArrays(nums2, nums1)
        if N2 == 0:
            return (nums1[(N1 - 1)/ 2] + nums1[N1 / 2]) / 2.0
        lo = 0
        hi = 2 * N2
        while lo <= hi:
            cut2 = (lo + hi) / 2
            cut1 = N1 + N2 - cut2
            L1 = float('-inf') if cut1 == 0 else nums1[(cut1 - 1) / 2]
            L2 = float('-inf') if cut2 == 0 else nums2[(cut2 - 1) / 2]
            R1 = float('inf') if cut1 == 2 * N1 else nums1[cut1 / 2]
            R2 = float('inf') if cut2 == 2 * N2 else nums2[cut2 / 2]
            if L1 > R2:
                lo = cut2 + 1
            elif L2 > R1:
                hi = cut2 - 1
            else:
                return (max(L1, L2) + min(R1, R2)) / 2.0






# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         len1 = len(nums1), len2 = len(nums2)
#         midl = (len1 + len2 + 1) / 2
#         midr = (len1 + len2 + 2) / 2
#         return self.getKth(nums1, nums2, 0, len1 - 1, 0, len2 - 1, midl)
#             + self.getKth(num1, num2, 0, len1 - 1, 0, len2 - 1, midr)
#
#
#     def getKth(self, nums1, nums2, l1, l2, r1, r2, k):
#         if k == 1:
#             if l1 > l2: return num2[0]
#             elif r1 > r2: return num1[0]
#             else: return min(num1[0], num2[0])
#         if nums1[mid1] == nums2[mid2]:
#             return nums1[mid1]
#         if nums1[mid1] <
