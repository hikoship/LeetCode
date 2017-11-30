# Generate Parentheses

# backtracking

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# recursion is easy
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(res, 0, 0, n, [])
        return res

    def dfs(self, res, left, right, n, prev):
        if left == n and right == n:
            res.append(''.join(prev))
            return
        if left < n:
            prev.append('(')
            self.dfs(res, left + 1, right, n, prev)
            prev.pop()
        if left > right:
            prev.append(')')
            self.dfs(res, left, right + 1, n, prev)
            prev.pop()




class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = []
        openPar = [i for i in range(n)]
        loc = n - 1
        arr = [list(openPar)]
        while loc > 0:
            openPar[loc] += 1
            if openPar[loc] > 2 * loc:
                # invalid
                openPar[loc] -= 1
                loc -= 1
                for i in range(loc + 1, n):
                    openPar[i] = openPar[loc] + i - loc + 1
            else:
                arr.append(list(openPar))
                loc = n - 1
        # print result
        res = []
        for e in arr:
            s = ''
            for i in range(2 * n):
                if i in e:
                    s += '('
                else:
                    s += ')'
            res.append(s)
        return res
