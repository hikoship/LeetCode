# Factorial Trailing Zeroes

# note numbers like 25 and 125. They have multiple 5 factors!

# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.

# iterative
class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        num = 0
        while n:
            n /= 5
            num += n
        return num

# recursive
class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        return 0 if n == 0 else n / 5 + self.trailingZeroes(n / 5)
