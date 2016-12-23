# Maximum Product of Word Lengths

# Use bit manipulation to represent whether a character is in a word

# Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.
#
# Example 1:
# Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
# Return 16
# The two words can be "abcw", "xtfn".
#
# Example 2:
# Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
# Return 4
# The two words can be "ab", "cd".
#
# Example 3:
# Given ["a", "aa", "aaa", "aaaa"]
# Return 0
# No such pair of words.

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        bitWords = []
        for word in words:
            bitWord = 0
            for char in word:
                bitWord |= 1 << ord(char) - ord('a')
            bitWords.append(bitWord)

        print bitWords

        res = 0
        l = len(words)
        for i in range(l):
            for j in range(i + 1, l):
                if bitWords[i] & bitWords[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res
