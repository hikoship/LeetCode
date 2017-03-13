# Valid numbers

# space, e, dot, +-...

# Validate if a given string is numeric.
#
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return False
        start = 0
        end = len(s) - 1
        while start < len(s) and s[start] == ' ':
            start += 1
        while end >= 0 and s[end] == ' ':
            end -= 1
        if start < len(s) and s[start] in '+-':
            start += 1
        if start > end:
            return False

        dot = False
        e = False
        firstIsNum = False
        dotFollowNum = False

        for i in range(start, end + 1):
            if '0' <= s[i] <= '9':
                continue
            elif s[i] == '.':
                # start == end: '.'
                if dot or e or start == end or (i == start and s[i + 1] == 'e'):
                    return False
                dot = True
            elif s[i] == 'e':
                if e or i == start or i == end:
                    return False
                e = True
            elif s[i] in '+-':
                if s[i - 1] != 'e' or i == end:
                    return False
            else:
                return False
        return True
