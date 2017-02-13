# Permutations II

# sort and jump over duplicated items

# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

# without copying
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        visited = [False] * len(nums)
        nums.sort()
        self.dfs(res, nums, visited, [])
        return res

    def dfs(self, res, nums, visited, prev):
        if len(prev) == len(nums):
            res.append(list(prev))
            return
        for i, n in enumerate(nums):
            if (i == 0 or nums[i] > nums[i - 1] or visited[i - 1]) and not visited[i]: # this condition is tricky!
                visited[i] = True
                prev.append(n)
                self.dfs(res, nums, visited, prev)
                prev.pop()
                visited[i] = False


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return []
        res = []
        nums.sort()
        self.dfs(res, nums, [])
        return res

    def dfs(self, res, nums, prev):
        if nums == []:
            res.append(prev)
        for i, n in enumerate(nums):
            if i == 0 or nums[i - 1] < n:
                self.dfs(res, nums[:i] + nums[i + 1:], prev + [n])
