class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # init
        chars = {}
        diffCount = 0 # count of chars with different occurrence numbers
        for c in t:
            if c in chars:
                chars[c] -= 1
            else:
                chars[c] = -1
                diffCount += 1
        left = 0
        right = 0
        res = s + '0' # to make it longer than s

        # loop
        while right < len(s):
            if diffCount == 0:
                if s[left] in chars:
                    if right - left < len(res):
                        res = s[left : right] # update res
                    if chars[s[left]] == 0:
                        diffCount += 1 # update diffCount
                    chars[s[left]] -= 1 # update chars
                left += 1
            else:
                if s[right] in chars:
                    chars[s[right]] += 1 # update chars
                    if chars[s[right]] == 0:
                        diffCount -= 1 # update diffCount
                right += 1

        # post process
        if diffCount == 0:
            while left < len(s):
                if s[left] in chars:
                    chars[s[left]] -= 1
                    if chars[s[left]] < 0:
                        if right - left < len(res):
                            res = s[left : right]
                        break
                left += 1

        return '' if len(res) > len(s) else res
