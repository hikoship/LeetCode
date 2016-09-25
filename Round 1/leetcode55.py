# Jump Game

# maintain the farthest element that has been visited instead of visited[].
# The former costs O(n) but the former is O(n^2).
# AFTER

# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# For example:
# A = [2,3,1,1,4], return true.
#
# A = [3,2,1,0,4], return false.

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length < 2:
            return True
        farthest = 0
        stack = [0]
        while len(stack) > 0:
            tmp = stack.pop()
            for i in range(tmp + nums[tmp], farthest, -1):
                if i >= length - 1:
                    return True
                stack.append(i)
            if tmp + nums[tmp] > farthest:
                farthest = tmp + nums[tmp]
        return False


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        for i in range(len(nums)):
            if reach >= i and i + nums[i] > reach:
                reach = i + nums[i]
        return reach >= i
