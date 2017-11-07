# Sudoku Solver

# back tracking

# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# Empty cells are indicated by the character '.'.
#
# You may assume that there will be only one unique solution.

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)


    def solve(self, board):
        i, j = self.nextEmpty(board)
        if i < 0:
            return True
        for x in '123456789':
            if self.isValid(board, i, j, x):
                board[i][j] = x
                if self.solve(board):
                    return True
                # WRONG: must restore board[i][j] (for validity checking)
                board[i][j] = '.'
        return False


    def nextEmpty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return i, j
        return -1, -1


    def isValid(self, board, i, j, x):
        # row
        for k in range(9):
            if board[i][k] == x:
                return False
        # column
        for k in range(9):
            if board[k][j] == x:
                return False
        # small grid
        for k in range(i - i % 3, i - i % 3 + 3):
            for l in range(j - j % 3, j - j % 3 + 3):
                if board[k][l] == x:
                    return False
        return True



# max recursion depth exceeded
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                for x in '123456789':
                    if self.isValid(board, i, j, x):
                        board[i][j] = x
                        if self.solveSudoku(board):
                            return True
                        # WRONG: must restore board[i][j] (for validity checking)
                        board[i][j] = '.'
                return False
        # WRONG: must return True
        return True

    def isValid(self, board, i, j, x):
        # row
        for k in range(9):
            if board[i][k] == x:
                return False
        # column
        for k in range(9):
            if board[k][j] == x:
                return False
        # small grid
        for k in range(i - i % 3, i - i % 3 + 3):
            for l in range(j - j % 3, j - j % 3 + 3):
                if board[k][l] == x:
                    return False
        return True
