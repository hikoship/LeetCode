# Text Justification

# ...

# Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
#
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.
#
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left justified and no extra space is inserted between words.
#
# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.
#
# Return the formatted lines as:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Note: Each word is guaranteed not to exceed L in length.
#
# click to show corner cases.
#
# Corner Cases:
# A line other than the last line might contain only one word. What should you do in this case?
# In this case, that line should be left-justified.


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        curWords = []
        curWidth = 0
        for w in words:
            if curWidth + len(w) <= maxWidth:
                curWords.append(w)
                curWidth += 1 + len(w)
            else:
                # BUG: edge case
                if len(curWords) == 1:
                    res.append(curWords[0] + ' ' * (maxWidth - len(curWords[0])))
                else:
                    curWidth -= 1 # BUG: don't forget to remove the last space
                    spaces = self.getSpaces(maxWidth - curWidth + len(curWords) - 1, len(curWords) - 1)
                    line = []
                    for i in range(len(curWords) - 1):
                        line.append(curWords[i])
                        line.append(' ' * spaces[i])
                    line.append(curWords[-1])
                    res.append(''.join(line))
                curWords = [w]
                curWidth = len(w) + 1
        line = ' '.join(curWords)
        res.append(line + ' ' * (maxWidth - len(line)))
        return res


    def getSpaces(self, spaceNum, slotNum):
        res = [spaceNum / slotNum] * slotNum
        for i in range(spaceNum % slotNum):
            res[i] += 1
        return res
