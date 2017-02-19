# Moving Average from Data Stream

# use array; use flag to record whether the array is full; use a cursor

# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
#
# For example,
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.past = [0] * size
        self.cur = 0
        self.isFull = False

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.size == 0:
            return 0
        if self.cur == self.size:
            self.isFull = True
            self.cur = 0
        self.past[self.cur] = val
        self.cur += 1
        if self.isFull:
            return sum(self.past) / float(self.size)
        else:
            return sum(self.past) / float(self.cur)




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
