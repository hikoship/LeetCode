# Permutations

# DFS

# Given a collection of distinct numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

# faster one without copying list
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        visited = [False] * len(nums)
        self.dfs(res, nums, visited, [])
        return res

    def dfs(self, res, nums, visited, prev):
        if len(prev) == len(nums):
            res.append(list(prev)) # Wrong: use copy!
            return
        for i, n in enumerate(nums):
            if not visited[i]:
                visited[i] =True
                prev.append(n)
                self.dfs(res, nums, visited, prev)
                prev.pop()
                visited[i] = False

# super slow
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return []
        return self.dfs(nums)

    def dfs(self, nums):
        l = len(nums)
        if l == 1:
            return [[nums[0]]]
        perm = []
        for i in range(l):
            subPerm = self.dfs(nums[:i] + nums[i + 1:])
            # this part is slow
            for p in subPerm:
                perm.append([nums[i]] + p)
        return perm

# faster one, but also slow to the death
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return []
        res = []
        self.dfs(res, nums, [])
        return res

    def dfs(self, res, nums, prev):
        l = len(nums)
        if l == 0:
            res.append(prev)
        for i in range(l):
            subPerm = self.dfs(res, nums[:i] + nums[i + 1:], prev + [nums[i]])
