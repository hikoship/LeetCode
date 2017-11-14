# Merge Intervals

# sort

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []:
            return []
        intervals.sort(key=lambda x: x.start)
        res = [Interval(intervals[0].start, intervals[0].end)]
        for i in intervals:
            if i.start <= res[-1].end:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(Interval(i.start, i.end))
        return res
