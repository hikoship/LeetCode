# Zigzag Iterator

# maintain global column; starting row is -1

# Given two 1d vectors, implement an iterator to return their elements alternately.
#
# For example, given two 1d vectors:
#
# v1 = [1, 2]
# v2 = [3, 4, 5, 6]
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].
#
# Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?
#
# Clarification for the follow up question - Update (2015-09-18):
# The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:
#
# [1,2,3]
# [4,5,6,7]
# [8,9]
# It should return [1,4,8,2,5,9,3,6,7].

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.matrix = [v1, v2]
        self.rowNum = len(self.matrix)
        self.colNum = 0
        for row in self.matrix:
            self.colNum = max(self.colNum, len(row))
        # WRONG: self.r = 0
        self.r = -1 # not 0. because matrix[0][0] is the 'next' element
        self.c = 0


    def next(self):
        """
        :rtype: int
        """
        # look for next in the same column
        for i in range(self.r + 1, self.rowNum):
            if self.c < len(self.matrix[i]):
                # find next in the same column
                self.r = i
                return self.matrix[self.r][self.c]
        # look for next in the next column
        self.c += 1
        for i in range(self.rowNum):
            if self.c < len(self.matrix[i]):
                # find next in the next column
                self.r = i
                return self.matrix[self.r][self.c]


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.colNum == 0:
            return False
        if self.c < self.colNum - 1:
            return True
        for i in range(self.r + 1, self.rowNum):
            if len(self.matrix[i]) == self.colNum:
                return True
        return False





# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
