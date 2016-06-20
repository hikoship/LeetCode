# Count Numbers with Unique Digits

# Permutation + DP

# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.
#
# Example:
# Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 9:
            n = 9
        a = [1, 10]
        for i in range(1, n):
            res = 1
            for j in range(i):
                res *= (9 - j)
            a.append(a[-1] + res * 9)
        return a[n]

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # enumeration; list is faster than if-else clause
        if n > 8:
            return 5611771
        a = [1, 10, 91, 739, 5275, 32491, 168571, 712891, 2345851]
        return a[n]
