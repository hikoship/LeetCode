# One Edit Distance

# recursive method exceeds the limit of memory. Compare char by char

# Given two strings S and T, determine if they are both one edit distance apart.

# optimized
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return False
        if len(s) < len(t):
            return self.isOneEditDistance(t, s)
        if len(s) - len(t) > 1:
            return False
        for i in range(len(t)):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i + 1:] == t[i + 1:]
                return s[i + 1:] == t[i:]
        # WRONG: don't omit this line: s/'abc', t/'ab'
        return True

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) < len(t):
            # make s no shorter than t
            return self.isOneEditDistance(t, s)
        if len(s) - len(t) > 1:
            return False
        for i in range(len(t)):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i + 1:] == t[i:]
        return len(s) > len(t)
