

# two end bfs, TLE
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        if beginWord in wordList:
            wordList.remove(beginWord)
        wordList.remove(endWord)
        res = []
        beginDict = {beginWord: [[beginWord]]}
        endDict = {endWord: [[endWord]]}
        breakFlag = False
        while len(beginDict) > 0 and len(endDict) > 0:
            newBegin = {}
            newEnd = {}
            visited = set()
            for w in beginDict:
                for i in range(len(w)):
                    for j in range(26):
                        tmp = w[:i] + chr(ord('a') + j) + w[i + 1:]
                        if tmp in endDict:
                            breakFlag = True
                            for beginList in beginDict[w]:
                                for endList in endDict[tmp]:
                                    res.append(beginList + endList)
                        if not breakFlag and tmp in wordList:
                            visited.add(tmp)
                            if tmp not in newBegin:
                                newBegin[tmp] = []
                            for beginList in beginDict[w]:
                                newBegin[tmp].append(beginList + [tmp])
            if breakFlag:
                break
            beginDict = newBegin
            for w in visited:
                wordList.remove(w)

            visited = set()
            for w in endDict:
                for i in range(len(w)):
                    for j in range(26):
                        tmp = w[:i] + chr(ord('a') + j) + w[i + 1:]
                        if tmp in beginDict:
                            breakFlag = True
                            for beginList in beginDict[tmp]:
                                for endList in endDict[w]:
                                    res.append(beginList + endList)
                        if not breakFlag and tmp in wordList:
                            if tmp not in newEnd:
                                newEnd[tmp] = []
                            for endList in endDict[w]:
                                newEnd[tmp].append([tmp] + endList)
            if breakFlag:
                break
            endDict = newEnd
            for w in visited:
                wordList.remove(w)
        return res
