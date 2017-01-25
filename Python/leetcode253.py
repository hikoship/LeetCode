# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

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
