# Shortest Word Distance III

# similar to 243. use only one index

# This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.
#
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
# word1 and word2 may be the same and they represent two individual words in the list.
#
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Given word1 = “makes”, word2 = “coding”, return 1.
# Given word1 = "makes", word2 = "makes", return 3.
#
# Note:
# You may assume word1 and word2 are both in the list.

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        prev = -1
        res = len(words)
        for i, w in enumerate(words):
            if w == word1 or w == word2:
                # WRONG: if prev >= 0:
                if prev >= 0 and (word1 == word2 or w != words[prev]): # only difference from leetcode #243
                    res = min(res, i - prev)
                prev = i
        return res
