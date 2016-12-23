# Single Number

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        value = 0
        for i in nums:
            value ^= i
        return value
