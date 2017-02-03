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
        res = []
        intervals.sort(key = operator.attrgetter('start'))
        start = intervals[0].start
        end = intervals[0].end
        for i in intervals:
            if i.start <= end:
                end = max(end, i.end)
            else:
                res.append([start, end])
                start = i.start
                end = i.end
        res.append([start, end])
        return res
