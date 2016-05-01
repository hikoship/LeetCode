# LeetCode 242
# Valid Anagram

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        # use hash table
        l = len(s)
        if l != len(t):
            return False

        # count the appearance of every character
        h_s = [0 for i in range(26)]
        h_t = [0 for i in range(26)]

        for i in range(l):
            h_s[ord(s[i]) - 97] += 1
            h_t[ord(t[i]) - 97] += 1

        for i in range(26):
            if h_s[i] != h_t[i]:
                return False

        return True
