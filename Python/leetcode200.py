# Number of Islands

# Union-find. A better solution is to use stack of recursion

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
# Answer: 3

class Solution(object):
    def __init__(self):
        self.parent = []
        self.size = []

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        self.parent = [i for i in range(m * n)]
        self.size = [1 for i in range(m * n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if i > 0 and grid[i - 1][j] == "1":
                        self.union(i * n + j, (i - 1) * n + j)
                    if j > 0 and grid[i][j - 1] == "1":
                        self.union(i * n + j, i * n + j - 1)
        res = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (not self.root(i * n + j) in res):
                    res.append(self.root(i * n + j))
        return len(res)

    def root(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.root(self.parent[i])
        return self.parent[i]

    def union(self, p, q):
        x = self.root(p)
        y = self.root(q)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            self.parent[x] = y
            self.size[y] += self.size[x]
        else:
            self.parent[y] = x
            self.size[x] += self.size[y]
        return
