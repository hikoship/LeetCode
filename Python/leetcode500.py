# Keyboard Row

# hashtable

# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
#
# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        d = {}
        for c in 'qwertyuiopQWERTYUIOP':
            d[c] = 1
        for c in 'asdfghjklASDFGHJKL':
            d[c] = 2
        for c in 'zxcvbnmZXCVBNM':
            d[c] = 3
        for w in words:
            row = d[w[0]]
            add = True
            for c in w:
                if d[c] != row:
                    add = False
                    break
            if add:
                res.append(w)
        return res
