# First Unique Character in a String

# one loop: use a dict, a set and a list. dict for positions, set for validation, list for result

# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

# one loop
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = []
        d = {}
        appear = set()
        for i, c in enumerate(s):
            if not c in appear:
                d[c] = i
                appear.add(c)
                pos.append(i)
            else:
                if c in d:
                    pos.remove(d[c])
                    del d[c]
        return pos[0] if pos != [] else -1


# two loops
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = [0] * 26
        for c in s:
            arr[ord(c) - ord('a')] += 1
        for i, c in enumerate(s):
            if arr[ord(c) - ord('a')] == 1:
                return i
        return -1
