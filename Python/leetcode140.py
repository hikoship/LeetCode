# Word Break II

# dp or dfs; need precheck

# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.
#
# Return all such possible sentences.
#
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
#
# A solution is ["cats and dog", "cat sand dog"].


# dfs, TLE without precheck
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        if not self.preCheck(s, wordDict):
            return []
        res = []
        self.dfs(s, wordDict, res, [], 0, 0)
        return res


    # LC139: word break 1
    def preCheck(self, s, wordDict):
        res = [False] * len(s)
        for i in range(len(s)):
            if s[:i + 1] in wordDict:
                res[i] = True
            else:
                for j in range(i):
                    if res[j] and s[j + 1 : i + 1] in wordDict:
                        res[i] = True
                        break
        return res[-1]


    def dfs(self, s, wordDict, res, prev, start, cur):
        if cur == len(s):
            if s[start:] in wordDict:
                prev.append(s[start:])
                res.append(' '.join(prev))
                prev.pop()
            return
        if s[start : cur + 1] in wordDict:
            prev.append(s[start : cur + 1])
            self.dfs(s, wordDict, res, prev, cur + 1, cur + 1)
            prev.pop()
        self.dfs(s, wordDict, res, prev, start, cur + 1)





# set, TLE without precheck
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        if not self.preCheck(s, wordDict):
            return []
        res = [set() for _ in s]
        for i in range(len(s)):
            if s[:i + 1] in wordDict:
                res[i].add(s[:i + 1])
            for j in range(i):
                if res[j] and s[j + 1 : i + 1] in wordDict:
                    for x in res[j]:
                        res[i].add(x + ' ' + s[j + 1 : i + 1])

        return list(res[-1])


    # LC139: word break 1
    def preCheck(self, s, wordDict):
        res = [False] * len(s)
        for i in range(len(s)):
            if s[:i + 1] in wordDict:
                res[i] = True
            else:
                for j in range(i):
                    if res[j] and s[j + 1 : i + 1] in wordDict:
                        res[i] = True
                        break
        return res[-1]
