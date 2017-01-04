# BFS
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        outDegree = {}
        inDegree = {}
        res = []
        for i in range(numCourses):
            inDegree[i] = set()
            outDegree[i] = set()
        for pre in prerequisites:
            x = pre[0]
            y = pre[1]
            inDegree[x].add(y)
            outDegree[y].add(x)
        stack = []
        for course in inDegree:
            if len(inDegree[course]) == 0:
                stack.append(course)
        while (stack):
            course = stack.pop()
            res.append(course)
            for out in outDegree[course]:
                inDegree[out].remove(course)
                if len(inDegree[out]) == 0:
                    stack.append(out)
        return res if len(res) == numCourses else []

# DFS
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        UNVISITED = 0
        VISITED = 1
        ONPATH = 2
        res = []
        outDegree = [set() for i in range(numCourses)]
        visitStatus = [UNVISITED for i in range(numCourses)]
        for pre in prerequisites:
            outDegree[pre[1]].add(pre[0])

        def isCycle(i):
            if visitStatus[i] == VISITED:
                return False
            elif visitStatus[i] == ONPATH:
                return True
            else:
                visitStatus[i] = ONPATH
                for out in outDegree[i]:
                    if isCycle(out):
                        return True
                visitStatus[i] = VISITED
                res.append(i)
                return False

        for i in range(numCourses):
            if isCycle(i):
                return []
        res.reverse()
        return res
