# Longest Consecutive Sequence

# hash; hash + union-find; set

# First turn the input into a set of numbers. That takes O(n) and then we can ask in O(1) whether we have a certain number.
#
# Then go through the numbers. If the number x is the start of a streak (i.e., x-1 is not in the set), then test y = x+1, x+2, x+3, ... and stop at the first number y not in the set. The length of the streak is then simply y-x and we update our global best with that. Since we check each streak only once, this is overall O(n). This ran in 44 ms on the OJ, one of the fastest Python submissions.
#
# def longestConsecutive(self, nums):
#     nums = set(nums)
#     best = 0
#     for x in nums:
#         if x - 1 not in nums:
#             y = x + 1
#             while y in nums:
#                 y += 1
#             best = max(best, y - x)
#     return best

# solution of @StefanPochmann
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        res = 0
        for n in s:
            if not n - 1 in s:
                # n is the first number of the sequence
                l = 1
                while n + l in s:
                    l += 1
                res = max(res, l)
        return res




# my union-find solution
class Solution(object):
    def __init__(self):
        self.parent = []
        self.size = []


    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        for i, n in enumerate(nums):
            d[n] = i

        # build disjoint set
        self.parent = range(len(nums))
        self.size = [1] * len(nums)

        for n in d:
            if n - 1 in d:
                self.union(d[n], d[n - 1])

        res = 0
        for i in range(len(nums)):
            res = max(res, self.size[i])

        return res



    def root(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.root(self.parent[i])
        return self.parent[i]

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        x = self.root(p)
        y = self.root(q)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            self.parent[x] = y
            self.size[y] += self.size[x]
        else:
            self.parent[y] = x
            self.size[x] += self.size[y]
        return
