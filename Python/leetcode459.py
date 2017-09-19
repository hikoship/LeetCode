# Repeated Substring Pattern

# check all possible substring length

# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
#
# Example 1:
# Input: "abab"
#
# Output: True
#
# Explanation: It's the substring "ab" twice.
# Example 2:
# Input: "aba"
#
# Output: False
# Example 3:
# Input: "abcabcabcabc"
#
# Output: True
#
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        subStrLen = [False] * (l / 2 + 1)
        # test all prime factors
        for i in range(1, l / 2 + 1):
            if l % i == 0:
                subStr = s[:i]
                if subStr * (l / i) == s:
                    return True
        return False

# slow
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        checkedRepeatNum = [False] * (l + 1)
        # test all prime factors
        for i in range(2, l + 1):
            if checkedRepeatNum[i]:
                continue
            if l % i == 0:
                subStr = s[: l / i]
                if subStr * i == s:
                    return True
            # marked all multiples of i as True
            for j in range(0, l + 1, i):
                checkedRepeatNum[j] = True
        return False
