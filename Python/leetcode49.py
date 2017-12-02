# Group Anagrams

# hash table + sort

# Given an array of strings, group anagrams together.
#
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:
#
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            tmp = self.code(s)
            if tmp not in d:
                d[tmp] = []
            d[tmp].append(s)
        return map(lambda x: d[x], d)

    def code(self, s):
        arr = [0] * 26
        for c in s:
            arr[ord(c) - ord('a')] += 1
        return ' '.join(map(str, arr))


# sort
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            tmp = ''.join(sorted(s))
            if tmp not in d:
                d[tmp] = []
            d[tmp].append(s)
        return map(lambda x: d[x], d)


# prime numbers, only for a-z
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        d = {}
        for s in strs:
            tmp = 1
            for c in s:
                tmp *= primes[(ord(c) - ord('a'))]
            if tmp in d:
                d[tmp].append(s)
            else:
                d[tmp] = [s]
        return [d[key] for key in d]
