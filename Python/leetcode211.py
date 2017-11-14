# Add and Search Word - Data structure design

# Trie; Recursively search

# Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
#
# For example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.

class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.isWord = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchHelper(word, 0, self.root)


    def searchHelper(self, word, start, node):
        if node is None:
            return False
        if start >= len(word):
            return node.isWord

        index = ord(word[start]) - ord('a')
        if 0 <= index < 26:
            return self.searchHelper(word, start + 1, node.children[index])
        for i in range(26):
            if self.searchHelper(word, start + 1, node.children[i]):
                return True
        return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
