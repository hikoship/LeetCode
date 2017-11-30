# Flip Game

# easy

# You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.
#
# Write a function to compute all possible states of the string after one valid move.
#
# For example, given s = "++++", after one move, it may become one of the following states:
#
# [
#   "--++",
#   "+--+",
#   "++--"
# ]
# If there is no valid move, return an empty list [].

# faster
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        sArr = list(s)
        count = 0
        for i, c in enumerate(s):
            if c == '+':
                count += 1
            else:
                count = 0
            if count >= 2:
                sArr[i] = '-'
                sArr[i - 1] = '-'
                res.append(''.join(sArr))
                sArr[i] = '+'
                sArr[i - 1] = '+'
        return res

class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        sArr = list(s)
        for i in range(1, len(s)):
            if s[i] == s[i - 1] and s[i] == '+':
                res.append(''.join(sArr[:i - 1] + ['-', '-'] + sArr[i + 1:]))
        return res
