# Decode Ways

# Recursion failed

# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if s == '' or s[0] == '0':
            return 0
        res = [1] * length
        if length > 1:
            if s[1] != '0':
                if s[0] == '1' and s[1] > '0' or s[0] == '2' and s[1] < '7':
                    res[1] = 2
                else:
                    res[1] = 1
            else:
                if s[0] == '1' or s[0] == '2':
                    res[1] = 1
                else:
                    return 0
        else:
            return 1

        for i in range(2, length):
            if s[i] != '0':
                if s[i - 1] == '1' or s[i - 1] == '2' and s[i] < '7':
                    res[i] = res[i - 2] + res[i - 1]
                else:
                    res[i] = res[i - 1]
            else:
                if s[i - 1] == '1' or s[i - 1] == '2':
                    res[i] = res[i - 2]
                else:
                    return 0
        print res
        return res[-1]

# a failed TLE solution
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if s == '' or s[0] == '0':
            return 0
        elif length == 1:
            return 1
        else:
            res = self.numDecodings(s[1:])
            if 0 < int(s[:2]) < 27:
                if length == 2:
                    res += 1
                else:
                    res += self.numDecodings(s[2:])
            return res
