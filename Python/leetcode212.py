# Word Search II

# build trie for words; dfs board; stop if no nodes in trie

# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
# For example,
# Given words = ["oath","pea","eat","rain"] and board =
#
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat","oath"].
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#
# click to show hint.
#
# You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
#
# If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.


# @yang.zheng.904 trie implementation
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if board == [] or words == []:
            return []
        trie = {}
        for w in words:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = w
        M = len(board)
        N = len(board[0])
        res = set()
        visited = [[False] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                self.dfs(board, M, N, i, j, trie, words, res, visited)
        return list(res)

    def dfs(self, board, M, N, i, j, trie, words, res, visited):
        if '#' in trie:
            res.add(trie['#'])
        if 0 <= i < M and 0 <= j < N and not visited[i][j] and board[i][j] in trie:
            visited[i][j] = True
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for d in dirs:
                self.dfs(board, M, N, i + d[0], j + d[1], trie[board[i][j]], words, res, visited)
            visited[i][j] = False





# TLE (lc208 is slow)
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if board == [] or words == []:
            return []
        trie = Trie()
        for w in words:
            trie.insert(w)
        M = len(board)
        N = len(board[0])
        res = set()
        visited = [[False] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if trie.root.children[ord(board[i][j]) - ord('a')]:
                    visited[i][j] = True
                    self.dfs(board, M, N, i, j, trie.root.children[ord(board[i][j]) - ord('a')], words, res, visited)
                    visited[i][j] = False
        return list(res)

    def dfs(self, board, M, N, i, j, root, words, res, visited):
        if root.word in words:
            res.add(root.word)
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for d in dirs:
            x = i + d[0]
            y = j + d[1]
            if 0 <= x < M and 0 <= y < N and not visited[x][y] and root.children[ord(board[x][y]) - ord('a')]:
                visited[x][y] = True
                self.dfs(board, M, N, x, y, root.children[ord(board[x][y]) - ord('a')], words, res, visited)
                visited[x][y] = False


# lc208 - implement trie
class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.word = None

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.word = word
