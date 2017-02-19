# Meeting Rooms II

# heap

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# this is WRONG for [[2,15],[36,45],[9,29],[16,23],[4,9]]
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        res = 0
        intervals.sort(key = lambda interval: interval.end)
        while intervals:
            end = 0
            i = 0
            while i < len(intervals):
                if intervals[i].start >= end:
                    end = intervals[i].end
                    intervals.remove(intervals[i])
                else:
                    i += 1
            res += 1
        return res



# O(nlogn), use heap
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals == []:
            return 0
        intervals.sort(key = operator.attrgetter('start'))
        # WRONG: rooms = heapq.heapify([0])
        rooms = [0]
        heapq.heapify(rooms) # the first room is idle after time 0
        for i in intervals:
            if i.start >= rooms[0]:
                heapq.heapreplace(rooms, i.end)
            else:
                heapq.heappush(rooms, i.end)
        return len(rooms)

# O(n^2)
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        res = 0
        intervals.sort(key = operator.attrgetter('start'))
        visited = [0] * len(intervals)
        num = 0
        while num < len(intervals):
            prev = 0
            for k, i in enumerate(intervals):
                if not visited[k] and i.start >= prev:
                    prev = i.end
                    visited[k] = 1
                    num += 1
            res += 1
        return res
