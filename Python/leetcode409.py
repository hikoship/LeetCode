# Longest Palindrome

# count number of appearance

# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        array = [0] * 128
        for c in s:
            array[ord(c)] += 1
        res = 0
        needCenter = True
        for x in array:
            res += x - x % 2
            if needCenter and x % 2:
                res += 1
                needCenter = False
        return res
