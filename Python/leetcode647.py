# Palindromic Substrings

# similar to lc5

# Given a string, your task is to count how many palindromic substrings in this string.
#
# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
#
# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# Note:
# The input string length won't exceed 1000.
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            res += self.helper(s, i, i)
            res += self.helper(s, i, i + 1)
        return res

    def helper(self, s, left, right):
        res = 0
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            else:
                break
        return res
