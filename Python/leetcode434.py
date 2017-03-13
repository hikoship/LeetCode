# Number of Segments in a String

# skip head spaces and add one if no tail spaces

# Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
#
# Please note that the string does not contain any non-printable characters.
#
# Example:
#
# Input: "Hello, my name is John"
# Output: 5

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        while i < len(s):
            if s[i] == ' ':
                res += 1
                while i < len(s) and s[i] == ' ':
                    i += 1
            else:
                i += 1
        if s and s[-1] != ' ':
            res += 1
        return res
