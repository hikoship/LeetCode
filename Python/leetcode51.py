# N-Queens

# maintain col, diag and anti-diag sets. dfs

# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
#
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

# beats 92%
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col = set()
        diag = set()
        antiDiag = set()
        res = []
        self.helper(res, n, [], col, diag, antiDiag)
        return res


    def helper(self, res, n, prev, col, diag, antiDiag):
        r = len(prev)
        if r == n:
            board = []
            for c in prev:
                board.append('.' * c + 'Q' + '.' * (n - c - 1))
            res.append(board)
            return
        for c in range(n):
            if c not in col and r - c not in diag and r + c not in antiDiag:
                col.add(c)
                diag.add(r - c)
                antiDiag.add(r + c)
                prev.append(c)
                self.helper(res, n, prev, col, diag, antiDiag)
                prev.pop()
                col.remove(c)
                diag.remove(r - c)
                antiDiag.remove(r + c)




# iterative
class Solution(object):
    def valid(self, loc, row, n):
        for i in range(n):
            if i != row and loc[i] != 0 and (loc[i] == loc[row] or loc[i] - loc[row] == i - row or loc[i] - loc[row] == row - i):
                return False
        return True

    def output(self, loc, n):
        board = []
        for i in range(n):
            board.append('.' * (loc[i] - 1) + 'Q' + '.' * (n - loc[i]))
        return board

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        loc = [0 for i in range(n)]
        row = 0
        res = []
        loc[row] = 1
        while row >= 0:
            while loc[row] <= n:
                if self.valid(loc, row, n):
                    if row == n - 1:
                        res.append(self.output(loc, n))
                        loc[row] += 1
                    else:
                        row += 1
                        loc[row] = 1
                else:
                    loc[row] += 1
            # no valid solution
            loc[row] = 0
            row -= 1
            loc[row] += 1
        return res
