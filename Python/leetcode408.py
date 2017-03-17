# Valid Word Abbreviation

# two pointers

# Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.
#
# A string such as "word" contains only the following valid abbreviations:
#
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".
#
# Note:
# Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.
#
# Example 1:
# Given s = "internationalization", abbr = "i12iz4n":
#
# Return true.
# Example 2:
# Given s = "apple", abbr = "a2e":
#
# Return false.

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = 0
        j = 0
        while i < len(word):
            print i, j
            if j >= len(abbr):
                return False
            elif word[i] == abbr[j]:
                i += 1
                j += 1
            # elif '0' <= abbr[j] <= '9':
            #     if abbr[j] == '0' and (j == 0 or not '0' <= abbr[j - 1] <= '9'):
            #         return False
            elif '1' <= abbr[j] <= '9':
                start = j
                while j < len(abbr) and '0' <= abbr[j] <= '9':
                    j += 1
                i += int(abbr[start : j])
            else:
                return False
        return i == len(word) and j == len(abbr)
