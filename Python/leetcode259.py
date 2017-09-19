class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = []
        visited = [False] * len(nums)
        self.NSum(nums, 0, visited, 0, 3, res, [])
        return res

    def NSum(self, nums, start, visited, target, N, res, prev):
        if N < 2 or N > len(nums):
            return
        if N == 2:
            # two sum
            
        else:
            # reduce NSum to (N-1)Sum
            for i in range(start, len(nums)):
                if N * nums[i] > target or N * nums[-1] < target:
                    break
                if not visited[i] and (i == 0 or nums[i] != nums[i - 1] or visited[i - 1]):
                    # remove duplicates
                    visited[i] = True
                    self.NSum(nums, i + 1, visited, target - nums[i], N - 1, res, prev + [nums[i]])
                    visited[i] = False
