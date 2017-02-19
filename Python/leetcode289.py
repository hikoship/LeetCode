# Game of Life

# Thought of the in-place solution by myself. Clever boy! But using 2-bit is more reasonable and intuitive.

# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
#
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state.
#
# Follow up:
# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 0: dead -> dead
        # 1: alive -> alive
        # 2: dead -> alive
        # 3: alive - >dead
        if board == []:
            return
        rowNum = len(board)
        colNum = len(board[0])
        for i in range(rowNum):
            for j in range(colNum):
                n = self.neigbor(board, i - 1, j) + self.neigbor(board, i + 1, j) + self.neigbor(board, i, j - 1) + self.neigbor(board, i, j + 1) + self.neigbor(board, i - 1, j - 1) + self.neigbor(board, i - 1, j + 1) + self.neigbor(board, i + 1, j - 1) + self.neigbor(board, i + 1, j + 1)
                if board[i][j] == 0 and n == 3:
                    board[i][j] = 2
                if board[i][j] == 1 and (n < 2 or n > 3):
                    board[i][j] = 3

        for i in range(rowNum):
            for j in range(colNum):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0

    def neigbor(self, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return 0
        else:
            # 0 / 2: dead
            # 1 / 3: alive
            return board[i][j] % 2
