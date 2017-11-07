# Longest Substring with At Most Two Distinct Characters

# same as lc340

# Given a string, find the length of the longest substring T that contains at most 2 distinct characters.
#
# For example, Given s = “eceba”,
#
# T is "ece" which its length is 3.
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        left = 0
        right = 0
        num = 0
        count = {}
        for c in s:
            count[c] = 0
        while right < len(s):
            if count[s[right]] == 0:
                num += 1
            count[s[right]] += 1
            while num > 2:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    num -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
