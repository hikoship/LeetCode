# @tqlong relaxing, O(n^2) + O(n) relaxing
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        dp = [i - 1 for i in range(N + 1)]
        for i in range(N):
            for j in range(N):
                if i - j < 0 or i + j >= N or s[i - j] != s[i + j]:
                    break
                dp[i + j + 1] = min(dp[i + j + 1], dp[i - j] + 1)
            for j in range(N):
                if i - j < 0 or i + j + 1 >= N or s[i - j] != s[i + j + 1]:
                    break
                dp[i + j + 2] = min(dp[i + j + 2], dp[i - j] + 1)
        return dp[-1]



# O(n^3) dp, TLE
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[float('inf') for _ in s] for _ in s]
        for i in range(len(s)):
            dp[i][i] = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if self.isPalindrome(s, i, j):
                    dp[i][j] = 0
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + 1)
        return dp[0][len(s) - 1]

    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
