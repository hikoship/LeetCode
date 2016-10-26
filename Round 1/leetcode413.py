# Arithmetic Slices

# two pointers / sliding window

# A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
#
# For example, these are arithmetic sequence:
#
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# The following sequence is not arithmetic.
#
# 1, 1, 2, 5, 7
#
# A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.
#
# A slice (P, Q) of array A is called arithmetic if the sequence:
# A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.
#
# The function should return the number of arithmetic slices in the array A.

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        start, end, res = 0, 2, 0
        if len(A) < 3:
            return 0
        diff = A[1] - A[0]
        while end < len(A):
            if A[end] - A[end - 1] == diff:
                end += 1
                if end == len(A):
                    res += (end - start - 1) * (end - start - 2) / 2
            else:
                res += (end - start - 1) * (end - start - 2) / 2
                start = end - 1
                diff = A[end] - A[start]
                end += 1
        return res
