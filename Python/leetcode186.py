# Reverse Words in a String II

# similar to leetcode189. remember to rotate the last word.

# Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.
#
# The input string does not contain leading or trailing spaces and the words are always separated by a single space.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
# Could you do it in-place without allocating extra space?

class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        self.reverse(s, 0, len(s) - 1)
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                self.reverse(s, start, i - 1)
                start = i + 1
        self.reverse(s, start, len(s) - 1) # WRONG: Don't forget this


    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
