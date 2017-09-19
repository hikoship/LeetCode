# Longest Palindromic Substring

# Use index to record string, not string itself.
# new: use a helper to return longest string with center of i

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example:
#
# Input: "babad"
#
# Output: "bab"
#
# Note: "aba" is also a valid answer.
# Example:
#
# Input: "cbbd"
#
# Output: "bb"

# new
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in range(len(s)):
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def helper(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        return s[left + 1 : right]





class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''
        l = len(s)
        i = 0
        minIdx = 0
        maxIdx = 0
        tmpMin = 0
        tmpMax = 0
        for i in range(l - 1):
            tmpMin = i
            tmpMax = i
            j = i + 1
            # even string
            if s[i] == s[j]:
                tmpMax = j
                while j < l - 1 and 2 * i >= j and s[j + 1] == s[2 * i - j]:
                    tmpMin -= 1
                    tmpMax += 1
                    j += 1
            if tmpMax - tmpMin > maxIdx - minIdx:
                minIdx = tmpMin
                maxIdx = tmpMax

            tmpMin = i
            tmpMax = i
            j = i + 1
            # odd string
            while j < l and 2 * i >= j and s[j] == s[2 * i - j]:
                tmpMin -= 1
                tmpMax += 1
                j += 1
            if tmpMax - tmpMin > maxIdx - minIdx:
                minIdx = tmpMin
                maxIdx = tmpMax
        return s[minIdx : maxIdx + 1]
