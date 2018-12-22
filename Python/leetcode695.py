# Max Area of Island

# same as lc200 number of islands

# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
#
# Example 1:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == []:
            return 0
        M = len(grid)
        N = len(grid[0])
        res = 0
        visited = [[False] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and not visited[i][j]:
                    res = max(res, self.dfs(grid, visited, M, N, i, j))
        return res

    def dfs(self, grid, visited, M, N, i, j):
        stack = [(i, j)]
        res = 1
        visited[i][j] = True
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while stack:
            p = stack.pop()
            for d in dirs:
                x = p[0] + d[0]
                y = p[1] + d[1]
                if 0 <= x < M and 0 <= y < N and grid[x][y] == 1 and not visited[x][y]:
                    stack.append((x, y))
                    visited[x][y] = True
                    res += 1
        return res
