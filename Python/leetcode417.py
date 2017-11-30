class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        M = len(matrix)
        if M == 0:
            return []
        N = len(matrix[0])
        res = []
        visitedPac = [[False] * N for _ in range(M)]
        visitedAtl = [[False] * N for _ in range(M)]
        stackPac = []
        stackAtl = []
        # init
        for i in range(M):
            visitedPac[i][0] = True
            visitedAtl[i][N - 1] = True
            stackPac.append((i, 0))
            stackAtl.append((i, N - 1))
        for j in range(N):
            visitedPac[0][j] = True
            visitedAtl[M - 1][j] = True
            stackPac.append((0, j))
            stackAtl.append((M - 1, j))
        # dfs
        self.dfs(matrix, M, N, stackPac, visitedPac)
        self.dfs(matrix, M, N, stackAtl, visitedAtl)
        # combine
        for i in range(M):
            for j in range(N):
                if visitedPac[i][j] and visitedAtl[i][j]:
                    res.append([i, j])
        return res


    def dfs(self, matrix, M, N, stack, visited):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while stack:
            pos = stack.pop()
            for d in dirs:
                i = pos[0] + d[0]
                j = pos[1] + d[1]
                # BUG: if not visited[i][j] and 0 <= i < M and 0 <= j < N and matrix[i][j] >= matrix[pos[0]][pos[1]]:
                if 0 <= i < M and 0 <= j < N and not visited[i][j] and matrix[i][j] >= matrix[pos[0]][pos[1]]:
                    visited[i][j] = True
                    stack.append((i, j))
