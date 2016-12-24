# Largest Number

# the first comparator I wrote is correct... so simple.

# Given a list of non negative integers, arrange them such that they form the largest number.
#
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
# Note: The result may be very large, so you need to return a string instead of an integer.

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        strList = [str(n) for n in nums] # make short numbers first
        strList.sort(reverse = True, cmp = self.comparator)
        res = "".join(strList)
        return "0" if res[0] == "0" else res

    def comparator(self, x, y):
        return int(x + y) - int(y + x)
