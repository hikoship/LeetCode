
# TLE
class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        if k <= 1 or len(str) <= 1:
            return str
        freq = {}
        prevPos = {}
        res = ''
        for c in str:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        for i in range(len(str)):
            valid = False
            freqChar = str[0]
            # Wrong: Don't forget these two lines below
            if freq[freqChar] > 0 and (freqChar not in prevPos or prevPos[freqChar] + k <= i):
                valid = True
            for c in freq:
                # Wrong: if freq[c] > freq[freqChar] and (not c in prevPos or prevPos[c] + k <= i):
                if freq[c] > 0 and (not valid or freq[c] > freq[freqChar]) and (not c in prevPos or prevPos[c] + k <= i):
                    freqChar = c
                    valid = True
            if not valid:
                return ''
            freq[freqChar] -= 1
            prevPos[freqChar] = i
            res += freqChar
        return res








# My WRONG SOLUTION: CANNOT DETECT ERROR
class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        # Don't forget this
        if k <= 1 or len(str) <= 1:
            return str
        # count frequency
        freq = {}
        for c in str:
            if c in freq:
                freq[c] += 1
                # Wrong: if freq[c] * k > len(str) + 1:
                if (freq[c] - 1) * k >= len(str)        :
                    return ''
            else:
                freq[c] = 1

        # sort
        import operator
        sortByFreq = []
        # Wrong: Don't ferget to add reverse=true
        for tup in sorted(freq.items(), key=operator.itemgetter(1), reverse=True):
            sortByFreq += [tup[0]] * tup[1]

        # rearrange
        res = [None] * len(str)
        count = 0
        start = 0
        while count < len(str):
            for i in range(start, len(str), k):
                res[i] = sortByFreq[count]
                count += 1
            start += 1
        output = ''
        for c in res:
            output += c
        return output
