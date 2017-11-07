# Valid Sudoku

# set

# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        square = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                if val in row[i]:
                    return False
                row[i].add(val)
                if val in col[j]:
                    return False
                col[j].add(val)
                if val in square[i / 3][j / 3]:
                    return False
                square[i / 3][j / 3].add(val)
        return True
