# improve: heap
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        points = set()
        left = {} # key: x; value: heights of buildings starting at x
        right = {} # key: x; value: heights of buildings ending at x
        for b in buildings:
            points.add(b[0])
            points.add(b[1])
            if b[0] not in left:
                left[b[0]] = []
            if b[1] not in right:
                right[b[1]] = []
            left[b[0]].append(b[2])
            right[b[1]].append(b[2])
        points = sorted(points)
        heap = [] # highest buildings over current point
        heapq.heapify(heap)
        heights = []
        for p in points:
            if p in left:
                for h in left[p]:
                    heapq.heappush(heap, -h)
            if p in right:
                for h in right[p]:
                    heap.remove(i)
            heights.append([p, max(map(lambda i: buildings[i][2], heap)) if heap else 0])
        res = [] # dedup
        for h in heights:
            if res == [] or h[1] != res[-1][1]:
                res.append(h)
        return res


# O(n^2), TLE https://briangordon.github.io/2014/08/the-skyline-problem.html
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        points = set()
        left = {} # key: x; value: list of indices of buildings starting at x
        right = {} # key: x; value: list of indices of buildings ending at x
        for i, b in enumerate(buildings):
            points.add(b[0])
            points.add(b[1])
            if b[0] not in left:
                left[b[0]] = []
            if b[1] not in right:
                right[b[1]] = []
            left[b[0]].append(i)
            right[b[1]].append(i)
        points = sorted(points)
        curSet = set() # list of indices of buildings over current point
        heights = []
        for p in points:
            if p in left:
                for i in left[p]:
                    curSet.add(i)
            if p in right:
                for i in right[p]:
                    curSet.remove(i)
            heights.append([p, max(map(lambda i: buildings[i][2], curSet)) if curSet else 0])
        res = [] # dedup
        for h in heights:
            if res == [] or h[1] != res[-1][1]:
                res.append(h)
        return res
