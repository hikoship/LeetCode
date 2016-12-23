# Word Search

# dfs

# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# For example,
# Given board =
#
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        v = [[False for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    if self.f(board, word, i, j, 1, v):
                        return True
        return False

    def f(self, board, word, i, j, idx, v):
        if idx == len(word):
            return True
        v[i][j] = True
        if i > 0:
            if word[idx] == board[i - 1][j] and not v[i - 1][j]:
                if self.f(board, word, i - 1, j, idx + 1, v):
                    return True
        if i < len(board) - 1:
            if word[idx] == board[i + 1][j] and not v[i + 1][j]:
                if self.f(board, word, i + 1, j, idx + 1, v):
                    return True
        if j > 0:
            if word[idx] == board[i][j - 1] and not v[i][j - 1]:
                if self.f(board, word, i, j - 1, idx + 1, v):
                    return True
        if j < len(board[0]) - 1:
            if word[idx] == board[i][j + 1] and not v[i][j + 1]:
                if self.f(board, word, i, j + 1, idx + 1, v):
                    return True
        v[i][j] = False
        return False
