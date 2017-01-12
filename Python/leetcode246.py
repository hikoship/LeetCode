# Strobogrammatic Number

# hashmap

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.
#
# For example, the numbers "69", "88", and "818" are all strobogrammatic.

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        # Wrong: for i in range((num + 1) / 2):
        for i in range((len(num) + 1) / 2):
            if not num[i] in d or d[num[i]] != num[len(num) - i - 1]:
                return False
        return True
