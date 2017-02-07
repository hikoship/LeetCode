# Find All Numbers Disappeared in an Array

# mark use index to record values. tricky!

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]

# O(n) + O(1) solution in discussion
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for n in nums:
            nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res


# my O(n) + O(n) solution
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(range(1, len(nums) + 1))
        for n in nums:
            if n in s:
                s.remove(n)
        return list(s)
