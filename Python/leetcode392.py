# Is Subsequence

# two pointers; loop

# Given a string s and a string t, check if s is subsequence of t.
#
# You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
#
# Example 1:
# s = "abc", t = "ahbgdc"
#
# Return true.
#
# Example 2:
# s = "axc", t = "ahbgdc"
#
# Return false.
#
# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == '':
            return True
        i = 0
        j = 0
        while i < len(t):
            if s[j] == t[i]:
                if j == len(s) - 1:
                    return True
                j += 1
            i += 1
        return False
