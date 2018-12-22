class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        res = 0
        index = 0
        lengths = map(len, sentence)
        for _ in range(rows):
            curLen = 0
            while curLen + lengths[index] <= cols:
                curLen += lengths[index] + 1
                index += 1
                if index == len(sentence):
                    index = 0
                    res += 1
        return res
    
# TLE
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        res = 0
        index = 0
        lengths = map(len, sentence)
        for _ in range(rows):
            curLen = 0
            while curLen + lengths[index] <= cols:
                curLen += lengths[index] + 1
                index += 1
                if index == len(sentence):
                    index = 0
                    res += 1
        return res
