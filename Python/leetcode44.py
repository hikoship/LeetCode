# Wildcard Matching

# similar to #10

# mplement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false



class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        M = len(s)
        N = len(p)
        res = [[False] * (N + 1) for _ in range(M + 1)]
        res[0][0] = True
        for j in range(1, N + 1):
            if p[j - 1] != '*':
                break
            res[0][j] = True
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if p[j - 1] == '*':
                    res[i][j] = res[i][j - 1] or res[i - 1][j]
                else:
                    res[i][j] = res[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '?')
        return res[M][N]
