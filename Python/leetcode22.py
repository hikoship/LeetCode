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