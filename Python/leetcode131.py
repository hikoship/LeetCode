# Palindrome Partitioning

# backtracking

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
        res = []
        self.dfs(s, res, 0, [])
        return res

    def dfs(self, s, res, start, prev):
        if start == len(s):
            res.append(list(prev))
            return
        for i in range(start, len(s)):
            if self.isPalindrome(s, start, i):
                prev.append(s[start : i + 1])
                self.dfs(s, res, i + 1, prev)
                prev.pop()

    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
