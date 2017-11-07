# Android Unlock Patterns

# DFS, record previous selected key and all other selected keys; hardcode all invalid situations

# Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.
#
# Rules for a valid pattern:
# Each pattern must connect at least m keys and at most n keys.
# All the keys must be distinct.
# If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
# The order of keys used matters.
#
# Explanation:
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
# Invalid move: 4 - 1 - 3 - 6
# Line 1 - 3 passes through key 2 which had not been selected in the pattern.
#
# Invalid move: 4 - 1 - 9 - 2
# Line 1 - 9 passes through key 5 which had not been selected in the pattern.
#
# Valid move: 2 - 4 - 1 - 3 - 6
# Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern
#
# Valid move: 6 - 5 - 4 - 1 - 9 - 2
# Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.
#
# Example:
# Given m = 1, n = 1, return 9.

class Solution(object):
    def __init__(self):
        self.res = 0
        self.jumpPairs = set([
        (1, 3), (4, 6), (7, 9),
        (1, 7), (2, 8), (3, 9),
        (1, 9), (3, 7)
        ])

    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        visited = set()
        self.dfs(m, n, visited, 0, 0)
        return self.res

    def dfs(self, m, n, visited, prev, count):
        if m <= count <= n:
            self.res += 1
        if count == n:
            return
        for x in range(1, 10):
            if x not in visited and self.noJump(x, prev, visited):
                visited.add(x)
                self.dfs(m, n, visited, x, count + 1)
                visited.remove(x)

    def noJump(self, x, y, visited):
        if (x, y) in self.jumpPairs or (y, x) in self.jumpPairs:
            return (x + y) / 2 in visited
        return True
