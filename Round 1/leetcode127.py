class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if beginWord == endWord:
            return 1
        wordList = set(wordList)
        l = len(wordList)
        res = 2
        prevCandidates = [beginWord]
        while len(wordList) > 0:
            if prevCandidates == []:
                return 0
            candidates = []
            for can in prevCandidates:
                for i in range(len(can)):
                    for j in range(26):
                        tmp = can[:i] + chr(ord('a') + j) + can[i + 1:]
                        if tmp == endWord:
                            return res
                        elif tmp in wordList:
                            candidates.append(tmp)
                            wordList.remove(tmp)
            prevCandidates = candidates
            res += 1
        return 0
