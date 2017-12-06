# Range Sum Query - Mutable

# binary indexed tree. how to get a value at index i? getSum(i) - getSum(i - 1). not self.tree[i]!!

# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# The update(i, val) function modifies nums by updating the element at index i to val.
# Example:
# Given nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# Note:
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is distributed evenly.

class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.tree = BinaryIndexedTree(nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.tree.update(i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.tree.getSum(j) - self.tree.getSum(i - 1)


class BinaryIndexedTree(object):
    def __init__(self, array):
        self.tree = [0] * (len(array) + 1)
        for i in range(len(array)):
            self.update(i, array[i])

    def update(self, i, val):
        diff = val - (self.getSum(i) - self.getSum(i - 1))
        i += 1
        while i < len(self.tree):
            self.tree[i] += diff
            i = self.getNext(i)

    def getSum(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i = self.getParent(i)
        return res

    # To get next
    # 1) 2's complement of get minus of index
    # 2) AND this with index
    # 3) Add it to index
    def getNext(self, i):
        return i + (i & -i)

    # To get parent
    # 1) 2's complement to get minus of index
    # 2) AND this with index
    # 3) Subtract that from index
    def getParent(self, i):
        return i - (i & -i)




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
