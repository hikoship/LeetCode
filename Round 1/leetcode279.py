# Perfect Squares

# store all squares in advance.

# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        sqList = []
        i = 1
        while i * i <= n:
            sqList.append(i * i)
            i += 1
        prev = {n} # prev and cur must be set, or MLE
        res = 0
        while prev:
            res += 1
            cur = set()
            for x in prev:
                for sq in sqList:
                    if x == sq:
                        return res
                    elif x < sq:
                        break
                    else:
                        cur.add(x - sq)
            prev = cur
        return res
