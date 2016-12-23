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
        res = []
        d = {}
        for s in strs:
            tmp = ''.join(sorted(s))
            if tmp in d:
                d[tmp].append(s)
            else:
                d[tmp] = [s]
        return [d[key] for key in d]
