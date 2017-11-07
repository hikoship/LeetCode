# Substring with Concatenation of All Words

# sliding window

# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
#
# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]
#
# You should return the indices: [0,9].
# (order does not matter).

# @GavinCode:
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if words == []:
            return []
        res = []
        length = len(words[0])
        count = {}
        for w in words:
            if w in count:
                count[w] += 1
            else:
                count[w] = 1
        for offset in range(length):
            tmp = {}
            start = offset
            added = 0
            for i in range(offset, len(s), length):
                subStr = s[i : i + length]
                if subStr in count:
                    added += 1
                    if subStr in tmp:
                        tmp[subStr] += 1
                    else:
                        tmp[subStr] = 1
                    while tmp[subStr] > count[subStr]:
                        # move left window
                        # WRONG: tmp[start : start + length] -= 1
                        tmp[s[start : start + length]] -= 1
                        added -= 1
                        start += length
                    if added == len(words):
                        res.append(start)
                else:
                    # invalid word
                    tmp = {}
                    start = i + length
                    added = 0
        return res


# my slow solution
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if words == []:
            return []
        res = []
        length = len(words[0])
        count = {}
        for w in words:
            if w in count:
                count[w] += 1
            else:
                count[w] = 1
        for i in range(len(s) - length * len(words) + 1):
            tmp = {}
            flag = True
            for j in range(len(words)):
                subStr = s[i + j * length: i + j * length + length]
                if subStr in tmp:
                    tmp[subStr] += 1
                else:
                    tmp[subStr] = 1
                if not (subStr in count and tmp[subStr] <= count[subStr]):
                    flag = False
                    break
            if flag:
                res.append(i)
        return res
