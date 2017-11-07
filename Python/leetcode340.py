# Longest Substring with At Most K Distinct Characters

# sliding window; not complex

# Given a string, find the length of the longest substring T that contains at most k distinct characters.
#
# For example, Given s = “eceba” and k = 2,
#
# T is "ece" which its length is 3.

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
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
            while num > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    num -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
