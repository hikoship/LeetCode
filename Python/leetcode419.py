# Battleships in a Board

# Be careful with Python list reference!!!

# >>> a = [[1] * 3]*3
# >>> a
# [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# >>> a[0][0] += 1
# >>> a
# [[2, 1, 1], [2, 1, 1], [2, 1, 1]]

# Given an 2D board, count how many different battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
#
# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
# Example:
# X..X
# ...X
# ...X
# In the above board there are 2 battleships.
# Invalid Example:
# ...X
# XXXX
# ...X
# This is not a valid board - as battleships will always have a cell separating between them.
# Your algorithm should not modify the value of the board.

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m = len(board)
        n = len(board[0])
        # NEVER USE checked = [[False] * n] * m !!!
        checked = [[False] * n for i in range(m)]
        cross = []
        res = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    cross.append((i, j))
        for tup in cross:
            i = tup[0]
            j = tup[1]
            if checked[i][j]:
                continue
            checked[i][j] = True
            res += 1
            for y in range(j + 1, n):
                if board[i][y] == 'X':
                    checked[i][y] = True
                else:
                    break

            for x in range(i + 1, m):
                if board[x][j] == 'X':
                    checked[x][j] = True
                else:
                    break
        return res
