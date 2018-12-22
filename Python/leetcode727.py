class Solution {
public:
    string minWindow(string S, string T) {
        int m = S.size(), n = T.size();
        vector<vector<int>> dp(n, vector<int>(m, -1));
        for (int i = 0; i < m; i++)
            if (S[i] == T[0]) dp[0][i] = i;
        for (int j = 1; j < n; j++) {
            int k = -1;
            for (int i = 0; i < m; i++) {
                if (k != -1 && S[i] == T[j]) dp[j][i] = k;
                if (dp[j-1][i] != -1) k = dp[j-1][i];
            }
        }
        int st = -1, len = INT_MAX;
        for (int i = 0; i < m; i++) {
            if (dp[n-1][i] != -1 && i-dp[n-1][i]+1 < len) {
                st = dp[n-1][i];
                len = i-dp[n-1][i]+1;
            }
        }
        return st == -1? "":S.substr(st, len);
    }
};

class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # dp[i][j]: start index of minWindow(S[:i + 1], T[:j + 1])
        M = len(s)
        N = len(T)
        dp = [[-1] * N for _ in range(M)]
        for i in range(M):
            if S[i] == T[0]:
                dp[i][0] == i
        for j in range(1, N):
            k = -1
            for i in range(M):
                if k != -1 and S[i] == T[j]:
                    dp[i][j] = k
                if dp[i][j - 1] != -1:
                    k = dp[i][j - 1]
        start = -1
        minLen = float('inf')
        for i in range(M):
            if dp[i][N - 1] and i - dp[i][N - 1] + 1 < minLen:
                start = dp[i][N - 1]
                minLen = i - dp[i][N - 1] + 1
        return '' if start == -1 else S[start: minLen]
