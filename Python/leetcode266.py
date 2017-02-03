# Palindrome Permutation

# If a list of chars can form a palindrome, at most one char appears odd times.

# Given a string, determine if a permutation of the string could form a palindrome.
#
# For example,
# "code" -> False, "aab" -> True, "carerac" -> True.
#
# Hint:
#
# Consider the palindromes of odd vs even length. What difference do you notice?
# Count the frequency of each character.
# If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?

# one pass
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars = set()
        for c in s:
            if c in chars:
                chars.remove(c)
            else:
                chars.add(c)
        return len(chars) < 2

# trival
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        nums = [0] * 128
        oddNum = 0
        for c in s:
            nums[ord(c)] += 1
        for n in nums:
            if n % 2:
                oddNum += 1
        return oddNum < 2
