# Longest Palindromic Substring

# Use index to record string, not string itself.

# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

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
