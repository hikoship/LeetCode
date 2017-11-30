# Longest Common Prefix

# easy

# Write a function to find the longest common prefix string amongst an array of strings.
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        maxLen = len(strs[0])
        for i in range(1, len(strs)):
            maxLen = min(maxLen, len(strs[i]))
            for j in range(maxLen):
                if strs[i - 1][j] != strs[i][j]:
                    maxLen = j
                    break
        return strs[0][:maxLen]
