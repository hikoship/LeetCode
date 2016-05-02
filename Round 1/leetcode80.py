# Remove Duplicates from Sorted Array II

# two pointers, 只要看 j 是不是和 i - 2 相同就可以了。不必删除n后续的部分

# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
#
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

# for unsorted?
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        l = len(nums)
        while j < l:
            nums[i] = nums[j]
            if j < l - 1:
                if nums[j + 1] != nums[j]:
                    i += 1
                    j += 1
                else:
                    nums[i + 1] = nums[j + 1]
                    j += 2
                    while j < l and nums[j] == nums[i]:
                        j += 1
                    i += 2
            else:
                del nums[i + 1:]
                return len(nums)

        del nums[i:]
        return len(nums)

# a easier approach
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l < 3:
            return l
        j = 2
        for i in range(2, l):
            while j < l and nums[j] == nums[i - 2]:
                j += 1
            if j < l:
                num[i] = nums[j]
                j += 1
            else:
                return i

# more concise approach
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l < 3:
            return l
        i = 2
        for j in range(2, l):
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        return i
