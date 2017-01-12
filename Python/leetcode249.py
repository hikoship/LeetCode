# Group Shifted Strings

# Hashmap. Use the shifted word starting with 'a' as the key.

# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
#
# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.
#
# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# A solution is:
#
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strings:
            tmp = self.shift(s)
            if tmp in d:
                d[tmp].append(s)
            else:
                d[tmp] = [s]
        return list(d.values()) # Python2: return d.values()

    def shift(self, s):
        res = ''
        # WRONG: diff = ord(s[0] - 'a')
        diff = ord(s[0]) - ord('a')
        for c in s:
            # WRONG: res.append(chr(ord(c) - diff))
            # WRONG: split to two conditions
            if ord(c) - ord('a') >= diff:
                res += chr(ord(c) - diff)
            else:
                # WRONG: res += chr(ord(c) + 25 - diff)
                res += chr(ord(c) + 26 - diff)
        return res # WRONG: if forget to return, the only key of the dict is "None".
