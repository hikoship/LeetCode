# Implement strStr()

# easy

# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1


# worst case time complexity: O(l1*l2) (s1 = 'aaaaaaaaaaaaaaaaaaaaab', s2 = 'aaaaab')
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l1 = len(haystack)
        l2 = len(needle)
        for i in range(l1 - l2 + 1):
            flag = True
            for j in range(l2):
                if haystack[i + j] != needle[j]:
                    flag = False
                    break
            if flag:
                return i
        return -1
