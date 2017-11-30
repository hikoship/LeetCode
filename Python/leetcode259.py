# 3Sum Smaller

# similar to k-sum, use res = end - start when nums[end] + nums[start] < target

# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
#
# For example, given nums = [-2, 0, 1, 3], and target = 2.
#
# Return 2. Because there are two triplets which sums are less than 2:
#
# [-2, 0, 1]
# [-2, 0, 3]
# Follow up:
# Could you solve it in O(n2) runtime?

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        nums.sort()
        return self.kSum(nums, 3, 0, target)


    def kSum(self, nums, k, start, target):
        if k == 2:
            return self.twoSum(nums, start, target)
        res = 0
        for i in range(start, len(nums)):
            res += self.kSum(nums, k - 1, i + 1, target - nums[i])
        return res


    def twoSum(self, nums, start, target):
        res = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] + nums[end] < target:
                res += end - start
                start += 1
            else:
                end -= 1
        return res
