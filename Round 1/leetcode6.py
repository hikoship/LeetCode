# LeetCode 6
# ZigZag Conversion

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        res = ''
        stepLength = 2 * numRows - 2
        for x in range(numRows):
            row = ''
            if 0 < x < numRows - 1:
                # middle lines
                i = x
                j = stepLength - x
                while i < len(s):
                    row += s[i]
                    if j < len(s):
                        row += s[j]
                    i += stepLength
                    j += stepLength
            else:
                # first and last line
                row = s[x::stepLength]
            res += row
        return res
