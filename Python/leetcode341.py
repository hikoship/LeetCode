# Flatten Nested List Iterator

# flatten first; or flatten when called

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.array = self.flatten(nestedList)
        self.cur = 0


    def next(self):
        """
        :rtype: int
        """
        self.cur += 1
        return self.array[self.cur - 1]


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur < len(self.array)


    def flatten(self, nestedList):
        res = []
        for x in nestedList:
            if x.isInteger():
                res.append(x.getInteger())
            else:
                # WRONG: for y in self.flatten(x):
                for y in self.flatten(x.getList()):
                    res.append(y)
        return res





# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
