# Shortest Unsorted Continuous Subarray

# two loops is intuitive

# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
#
# You need to find the shortest such subarray and output its length.
#
# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.

# my optimization: no stack; O(n) + O(1)
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        flag = False
        for i in range(1, len(nums)):
            while left >= 0 and nums[i] < nums[left]:
                flag = True
                left -= 1
            if not flag:
                left += 1
        right = len(nums) - 1
        flag = False
        # BUG: BIG: for i in range(len(nums) - 1, 0, -1):
        for i in range(len(nums) - 2, -1, -1):
            while right < len(nums) and nums[i] > nums[right]:
                flag = True
                right += 1
            if not flag:
                right -= 1
        print left, right
        return max(0, right - left - 1)




# my solution: two loops + stack + flag. beats 86%. O(n) + O(n)
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = []
        flag = False
        for i in range(len(nums)):
            while left and nums[i] < left[-1]:
                flag = True
                left.pop()
            if not flag:
                left.append(nums[i])
        right = []
        flag = False
        for i in range(len(nums) - 1, -1, -1):
            while right and nums[i] > right[-1]:
                flag = True
                right.pop()
            if not flag:
                right.append(nums[i])
        # BUG: return len(nums) - len(left) - len(right)
        return max(0, len(nums) - len(left) - len(right))
