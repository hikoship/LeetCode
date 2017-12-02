# N-Queens II

# same as lc51. when i say same, i mean exactly same.

# Follow up for N-Queens problem.
#
# Now, instead outputting board configurations, return the total number of distinct solutions.


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        col = set()
        diag = set()
        antiDiag = set()
        res = [0]
        self.helper(res, n, [], col, diag, antiDiag)
        return res[0]


    def helper(self, res, n, prev, col, diag, antiDiag):
        r = len(prev)
        if r == n:
            res[0] += 1
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
