# Implement Trie (Prefix Tree)

# collections.defaultdict improves performance

# Codes in comments lead to TLE
class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isWord = False
        # self.children = {}
        # for i in range(ord('a'), ord('z') + 1):
        #     self.children[chr(i)] = None

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            # if node.children[c] is None:
            #     node.children[c] = Node()
            node = node.children[c]
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            node = node.children.get(c)
            # WRONG: if node.children is None:
            if node is None:
                return False
        return node.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            node = node.children.get(c)
            # WRONG: if node.children is None:
            if node is None:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
