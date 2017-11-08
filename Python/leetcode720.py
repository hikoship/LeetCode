# Longest Word in Dictionary

# one edit distance. note: new char can be inserted at any position (word -> world)

# Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.
#
# If there is no answer, return the empty string.
# Example 1:
# Input:
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation:
# The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
# Example 2:
# Input:
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation:
# Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
# Note:
#
# All the strings in the input will only contain lowercase letters.
# The length of words will be in the range [1, 1000].
# The length of words[i] will be in the range [1, 30].

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        maxLen = 0
        for w in words:
            maxLen = max(maxLen, len(w))
        lengths = [[] for _ in range(maxLen + 2)]
        for w in words:
            lengths[len(w)].append(w)
        visited = set()
        stack = list(lengths[1])
        res = ''
        while stack:
            w = stack.pop()
            # WRONG: if len(w) > res or len(w) == res and w < res:
            if len(w) > len(res) or len(w) == len(res) and w < res:
                res = w
            for x in lengths[len(w) + 1]:
                if x not in visited and self.isValid(w, x):
                    stack.append(x)
                    visited.add(x)
        return res


    def isValid(self, x, y):
        if len(y) - len(x) != 1:
            return False
        for i in range(len(x)):
            if x[i] != y[i]:
                return x[i:] == y[i + 1:]
        return True
