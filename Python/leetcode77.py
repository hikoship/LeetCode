# Combinations

# backtracking. Note that List.append() just copies pointers.

# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# For example,
# If n = 4 and k = 2, a solution is:
#
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(res, n, k, [], 1)
        return res

    def helper(self, res, n, k, prev, start):
        if n - start + 1 < k - len(prev):
            # remaining numbers < numbers needed
            return
        if len(prev) == k:
            res.append(list(prev))
            return
        for i in range(start, n + 1):
            prev.append(i)
            self.helper(res, n, k, prev, i + 1)
            prev.pop()





class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        a = range(1, k + 1)
        res = []
        while True:
            cur = k - 1
            while a[cur] <= n:
                res.append(a[:])
                a[cur] += 1
            while a[cur] > n - k + cur:
                cur -= 1
                if cur < 0:
                    return res
            a[cur] += 1
            for i in range(cur + 1, k):
                a[i] = a[cur] + i - cur
