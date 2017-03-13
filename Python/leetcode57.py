# Insert Interval

# edge cases

# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their start times.
#
# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
#
# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
#
# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# solution by @shpolsky
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        i = 0
        while i < len(intervals) and newInterval.start > intervals[i].end:
            res.append(intervals[i])
            i += 1

        # intersection starts
        temp = Interval(newInterval.start, newInterval.end)
        while i < len(intervals) and temp.end >= intervals[i].start:
            temp = Interval(min(temp.start, intervals[i].start), max(temp.end, intervals[i].end))
            i += 1
        res.append(temp)

        # intersection ends
        return res + intervals[i:]

# my solution
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # empty
        if intervals == []:
            return [newInterval]
        # leftmost
        if newInterval.end < intervals[0].start:
            return [newInterval] + intervals
        # rightmost
        if newInterval.start > intervals[-1].end:
            return intervals + [newInterval]
        for i, elem in enumerate(intervals):
            # inner
            if elem.start <= newInterval.start <= newInterval.end <= elem.end:
                return intervals
            # outer
            if newInterval.end < elem.start and (i == 0 or newInterval.start > intervals[i - 1].end):
                return intervals[:i] + [newInterval] + intervals[i:]
            # merge
            if newInterval.start <= elem.end:
                j = i + 1
                while j < len(intervals) and newInterval.end >= intervals[j].start:
                    j += 1
                return intervals[:i] + [Interval(min(newInterval.start, intervals[i].start), max(newInterval.end, intervals[j - 1].end))] + intervals[j:]
