# Word Ladder

# two end and meet at middle

# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
# 
# Only one letter can be changed at a time
# Each intermediate word must exist in the word list
# For example,
# 
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# 
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.

# two end bfs
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList = set(wordList)
        wordList.remove(beginWord)
        wordList.remove(endWord)
        res = 2
        beginSet = ({beginWord})
        endSet = ({endWord})
        while len(beginSet) > 0 and len(endSet) > 0:
            newBegin = set()
            newEnd = set()
            for w in beginSet:
                for i in range(len(w)):
                    for j in range(26):
                        tmp = w[:i] + chr(ord('a') + j) + w[i + 1:]
                        if tmp in endSet:
                            return res
                        if tmp in wordList:
                            newBegin.add(tmp)
                            wordList.remove(tmp)
            beginSet = newBegin
            res += 1
            for w in endSet:
                for i in range(len(w)):
                    for j in range(26):
                        tmp = w[:i] + chr(ord('a') + j) + w[i + 1:]
                        if tmp in beginSet:
                            return res
                        if tmp in wordList:
                            newEnd.add(tmp)
                            wordList.remove(tmp)
            endSet = newEnd
            res += 1
        return 0 



# one-end bfs
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList = set(wordList)
        res = 2
        prevCandidates = set({beginWord})
        while len(wordList) > 0:
            if len(prevCandidates) == 0:
                return 0
            candidates = set({})
            for can in prevCandidates:
                for i in range(len(can)):
                    for j in range(26):
                        tmp = can[:i] + chr(ord('a') + j) + can[i + 1:]
                        if tmp == endWord:
                            return res
                        elif tmp in wordList:
                            candidates.add(tmp)
                            wordList.remove(tmp)
            prevCandidates = candidates
            res += 1
        return 0
