# Shortest Word Distance II

# Hashmap. O(n) time complexity

# This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?
#
# Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.
#
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.
#
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
#
# Show Company Tags
# Show Tags
# Hide Similar Problems

# Just copy leetcode 243 to shortest() methods will cause TLE.
class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.d = {}
        for i, w in enumerate(words):
            if w in self.d:
                self.d[w].append(i)
            else:
                self.d[w] = [i]


    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = self.d[word1]
        l2 = self.d[word2]
        i, j = 0, 0
        res = abs(l1[0] - l2[0]) # WRONG: Don't forget to initialize res
        while i < len(l1) and j < len(l2):
            res = min(res, abs(l1[i] - l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return res



# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
