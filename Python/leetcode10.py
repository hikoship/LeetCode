# Regular Expression Matching

# DP. Discuss '*' and other chars
# for '*': res[i][j] = res[i][j - 2](match 0 chars) or res[i - 1][j](previous matches) and (s[i - 1] == p[j - 2] or p[j - 2] == '.')(current matches)
# for other chars: res[i][j] = res[i - 1][j - 1](previous matches) and s[i - 1] == p[j - 1](current matches)

# Implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
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
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true


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
        for j in range(1, N, 2):
            if p[j] != '*':
                break
            res[0][j + 1] = True
        res[0][0] = True
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if p[j - 1] == '*':
                    res[i][j] = res[i][j - 2] or res[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.')
                else:
                    res[i][j] = res[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
        return res[M][N]



# can merge '.' and 'abc...'; unnecessary to judge res[i][j - 1]
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
        for j in range(2, N + 1, 2):
            if p[j - 1] == '*' and p[j - 2] != '*':
                res[0][j] = True
            else:
                break
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if p[j - 1] == '.':
                    res[i][j] = res[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if j - 1 == 0 or p[j - 2] == '*':
                        # invalid
                        return False
                    elif p[j - 2] == '.':
                        res[i][j] = res[i][j - 2] or res[i][j - 1] or res[i - 1][j]
                    else:
                        res[i][j] = res[i][j - 2] or res[i][j - 1] or (res[i - 1][j] and s[i - 1] == p[j - 2])
                else:
                    res[i][j] = res[i - 1][j - 1] and s[i - 1] == p[j - 1]
        return res[M][N]
