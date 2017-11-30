# Add Bold Tag in String

# find + merge intervals

# Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
#
# Example 1:
# Input:
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"
# Example 2:
# Input:
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"
# Note:
# The given dict won't contain duplicates, and its length won't exceed 100.
# All the strings in input have length in range [1, 1000].

class Solution(object):
    def addBoldTag(self, s, d):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        intervals = []
        for word in d:
            i = 0
            while True:
                i = s.find(word, i)
                if i == -1:
                    break
                intervals.append([i, i + len(word)])
                i += 1
        mergedIntervals = self.merged(intervals)
        strArr = []
        start = 0
        for i in mergedIntervals:
            strArr.append(s[start: i[0]])
            strArr.append('<b>')
            strArr.append(s[i[0]: i[1]])
            strArr.append('</b>')
            start = i[1]
        strArr.append(s[start:])
        return ''.join(strArr)



    # lc56
    def merged(self, intervals):
        if intervals == []:
            return []
        intervals.sort()
        res = [list(intervals[0])]
        for i in intervals:
            if i[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append([i[0], i[1]])
        return res
