# Surrounded Regions

# similar to #200

# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X

class Solution(object):
    def __init__(self):
        self.parent = []
        self.size = []

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        edge = []
        self.parent = [i for i in range(m * n)]
        self.size = [1 for i in range(m * n)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    if (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                        edge.append(i * n + j);
                    if i > 0 and board[i - 1][j] == "O":
                        self.union(i * n + j, (i - 1) * n + j)
                    if j > 0 and board[i][j - 1] == "O":
                        self.union(i * n + j, i * n + j - 1)
        res = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (not self.root(i * n + j) in res):
                    res.append(self.root(i * n + j))

        # skip edge islands
        for x in edge:
            if self.root(x) in res:
                res.remove(self.root(x))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and self.root(i * n + j) in res:
                    board[i][j] = "X"
        return

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
