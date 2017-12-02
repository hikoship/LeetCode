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
        count = {}
        for w in words:
            if w not in count:
                count[w] = 0
            count[w] += 1
        wordLen = len(words[0])
        res = []
        for offset in range(wordLen):
            curCount = {}
            start = offset
            added = 0
            for i in range(offset, len(s), wordLen):
                subStr = s[i : i + wordLen]
                if subStr in count:
                    added += 1
                    if subStr not in curCount:
                        curCount[subStr] = 0
                    curCount[subStr] += 1
                    while curCount[subStr] > count[subStr]:
                        # move left window
                        # WRONG: curCount[start : start + wordLen] -= 1
                        curCount[s[start : start + wordLen]] -= 1
                        added -= 1
                        start += wordLen
                    if added == len(words):
                        res.append(start)
                else:
                    # invalid word
                    curCount = {}
                    start = i + wordLen
                    added = 0
        return res


# TLE
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        count = {}
        for w in words:
            if w not in count:
                count[w] = 0
            count[w] += 1
        wordLen = len(words[0])
        res = []
        for i in range(len(s)):
            curCount = {}
            added = 0
            for w in words:
                curCount[w] = 0
            for j in range(i, len(s), wordLen):
                subStr = s[j: j + wordLen]
                if subStr not in count or curCount[subStr] == count[subStr]:
                    break
                curCount[subStr] += 1
                added += 1
                if added == len(words):
                    res.append(i)
        return res
