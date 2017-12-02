# Sudoku Solver

# back tracking

# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# Empty cells are indicated by the character '.'.
#
# You may assume that there will be only one unique solution.

# pre-process valid set and empty cells array. beats 89%
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        square = [[set() for _ in range(3)] for _ in range(3)]
        empty = []
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    empty.append([i, j])
                else:
                    row[i].add(val)
                    col[j].add(val)
                    square[i / 3][j / 3].add(val)
        self.solve(board, row, col, square, empty, 0)


    def solve(self, board, row, col, square, empty, emptyIndex):
        if emptyIndex == len(empty):
            return True
        i, j = empty[emptyIndex]
        for x in '123456789':
            if x in row[i] or x in col[j] or x in square[i / 3][j / 3]:
                continue
            board[i][j] = x
            row[i].add(x)
            col[j].add(x)
            square[i / 3][j / 3].add(x)
            if self.solve(board, row, col, square, empty, emptyIndex + 1):
                return True
            # WRONG: must restore board[i][j] (for validity checking)
            board[i][j] = '.'
            row[i].remove(x)
            col[j].remove(x)
            square[i / 3][j / 3].remove(x)
        return False
