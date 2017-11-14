# Generalized Abbreviation

# two conditions: 1. s[i] is abbr.; 2. s[i] is letter

# Write a function to generate the generalized abbreviations of a word.
#
# Example:
# Given word = "word", return the following list (order does not matter):
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
#

# @yavinci
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        self.dfs(word, res, 0, [], 0)
        return res


    def dfs(self, s, res, start, prev, count):
        if start == len(s):
            if count > 0:
                prev.append(str(count))
            res.append(''.join(prev))
            if count > 0:
                prev.pop()
        else:
            self.dfs(s, res, start + 1, prev, count + 1)
            if count > 0:
                prev.append(str(count))
            prev.append(s[start])
            self.dfs(s, res, start + 1, prev, 0)
            prev.pop()
            if count > 0:
                prev.pop()
