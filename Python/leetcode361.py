# Bomb Enemy

# dp
# scan from top-left to bottom-right to get up and left number of enemies;
# scan from bottom-right to top-left to get down and right number of enemies;

# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
# Note that you can only put the bomb at an empty cell.
#
# Example:
# For the given grid
#
# 0 E 0 0
# E 0 W E
# 0 E 0 0
#
# return 3. (Placing a bomb at (1,1) kills 3 enemies)

# beat 97%
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        M = len(grid)
        N = len(grid[0])
        up = [[0] * N for _ in range(M)]
        down = [[0] * N for _ in range(M)]
        left = [[0] * N for _ in range(M)]
        right = [[0] * N for _ in range(M)]
        res = 0
        if grid[0][0] == 'E':
            up[0][0] = 1
            left[0][0] = 1
        for i in range(1, M):
            if grid[i][0] == 'E':
                up[i][0] = up[i - 1][0] + 1
                left[i][0] = 1
            elif grid[i][0] == '0':
                up[i][0] = up[i - 1][0]
        for j in range(1, N):
            if grid[0][j] == 'E':
                left[0][j] = left[0][j - 1] + 1
                up[0][j] = 1
            elif grid[0][j] == '0':
                left[0][j] = left[0][j - 1]
        for i in range(1, M):
            for j in range(1, N):
                if grid[i][j] == 'E':
                    up[i][j] = up[i - 1][j] + 1
                    left[i][j] = left[i][j - 1] + 1
                # BUG: elif grid[0][j] == '0':
                elif grid[i][j] == '0':
                    up[i][j] = up[i - 1][j]
                    left[i][j] = left[i][j - 1]
        if grid[M - 1][N - 1] == 'E':
            down[M - 1][N - 1] = 1
            right[M - 1][N - 1] = 1
        for i in range(M - 2, -1, -1):
            if grid[i][N - 1] == 'E':
                down[i][N - 1] = down[i + 1][N - 1] + 1
                right[i][N - 1] = 1
            elif grid[i][N - 1] == '0':
                down[i][N - 1] = down[i + 1][N - 1]
                res = max(res, up[i][N - 1] + left[i][N - 1] + down[i][N - 1] + right[i][N - 1])
        for j in range(N - 2, -1, -1):
            if grid[M - 1][j] == 'E':
                right[M - 1][j] = right[M - 1][j + 1] + 1
                down[M - 1][j] = 1
            elif grid[M - 1][j] == '0':
                right[M - 1][j] = right[M - 1][j + 1]
                res = max(res, up[M - 1][j] + left[M - 1][j] + down[M - 1][j] + right[M - 1][j])
        for i in range(M - 2, -1, -1):
            for j in range(N - 2, -1, -1):
                if grid[i][j] == 'E':
                    down[i][j] = down[i + 1][j] + 1
                    right[i][j] = right[i][j + 1] + 1
                elif grid[i][j] == '0':
                    down[i][j] = down[i + 1][j]
                    right[i][j] = right[i][j + 1]
                    res = max(res, up[i][j] + left[i][j] + down[i][j] + right[i][j])
        return res
