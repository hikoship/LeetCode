# Course Schedule

# Two methods

# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# For example:
#
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
#
# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
#
# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
#
# click to show more hints.
#
# Hints:
# This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
# Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
# Topological sort could also be done via BFS.

# BFS
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        outDegree = {}
        inDegree = {}
        res = 0
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
            res += 1
            for out in outDegree[course]:
                inDegree[out].remove(course)
                if len(inDegree[out]) == 0:
                    stack.append(out)
        return res == numCourses

# DFS
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        UNVISITED = 0
        VISITED = 1
        ONPATH = 2
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
                return False

        for i in range(numCourses):
            if isCycle(i):
                return False
        return True
