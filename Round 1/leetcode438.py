# Find All Anagrams in a String

# dictionary and count

# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

# O(n)
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        res = []
        target = {}
        cur = {}
        count = 0
        for c in p:
            if c in target:
                target[c] += 1
            else:
                target[c] = 1
            cur[c] = 0

        # initialize cur
        for i in range(len(p)):
            if s[i] in cur:
                cur[s[i]] += 1
                if cur[s[i]] == target[s[i]]:
                    count += 1
        if count == len(cur):
            res.append(0)

        for i in range(len(s) - len(p)):
            if s[i] in cur:
                if cur[s[i]] == target[s[i]]:
                    count -= 1
                cur[s[i]] -= 1
            if s[i + len(p)] in cur:
                cur[s[i + len(p)]] += 1
                if cur[s[i + len(p)]] == target[s[i + len(p)]]:
                    count += 1
                    if count == len(cur):
                        res.append(i + 1)

        return res


# O(nplogp),TLE
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        p.sort()
        for i in range(len(s) - len(p) + 1):
            if not s[i] in p:
                continue
            if sorted(s[i : i + len(p)]) == p:
                res.append(i)
        return res
