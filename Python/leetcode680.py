# Valid Palindrome II

# easy

# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

# O(n)
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.helper(s, left + 1, right) or self.helper(s, left, right - 1)
            left += 1
            right -= 1
        return True


    def helper(self, s, start, end):
        left = start
        right = end
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
