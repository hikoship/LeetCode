
# Given a string s, partition s such that every substring of the partition is a palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# For example, given s = "aab",
# Return
# 
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        d = {}
        d[-1] = [[]]
        for i in range(len(s)):
            d[i] = []
            for j in range(i + 1):
                if self.isPalindrome(s[j : i + 1]):
                    for x in d[j - 1]:
                        d[i].append(x + [s[j : i + 1]])
        return d[len(s) - 1]

    def isPalindrome(self, s):
        for i in range(len(s) / 2):
            if s[i] != s[-1 - i]:
                return False
        return True