# Word Break

# DP; Initialize all boolean value false

# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
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
