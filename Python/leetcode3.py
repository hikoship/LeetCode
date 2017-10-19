# Longest Substring Without Repeating Characters

# two pointers and hash table

# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# clean
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        left = 0
        right = 0
        chars = set()
        while right < len(s):
            if s[right] in chars:
                chars.remove(s[left])
                left += 1
            else:
                chars.add(s[right])
                right += 1
                res = max(res, right - left)
        return res


# old
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        start, end = 0, 1
        res = 1
        if l == 0:
            return 0
        hasChar = {s[0]: True}
        while end < l:
            if s[end] in hasChar:
                res = max(res, end - start)
                while s[end] in hasChar:
                    del hasChar[s[start]]
                    start += 1
            hasChar[s[end]] = True
            end += 1
        return max(res, end - start)
