# Course Schedule II

# Note DFS method

# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
#
# For example:
#
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]
#
# 4, [[1,0],[2,0],[3,1],[3,2]]
# There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].
#
# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
#
# click to show more hints.
#
# Hints:
# This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
# Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
# Topological sort could also be done via BFS.

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
