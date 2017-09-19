class Solution(object):
    def __init__(self):
        self.res = 0

    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        visited = [False] * 10
        self.dfs(m, n, visited, 0, 0)
        return self.res

    def dfs(self, m, n, visited, prev, count):
        if m <= count <= n:
            self.res += 1
        if count == n:
            return
        if count == 0:
            for i in range(1, 10):
                visited[i] = True
                self.dfs(m, n, visited, i, count + 1)
                visited[i] = False
        else:
            for i in [prev - 1, prev + 1, prev - 3, prev + 3]:
                if 1 <= i <= 9 and not visited[i]:
                    visited[i] = True
                    self.dfs(m, n, visited, i, count + 1)
                    visited[i] = False
