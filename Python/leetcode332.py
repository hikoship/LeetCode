class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = {}
        for t in tickets:
            if t[0] not in graph:
                graph[t[0]] = []
            graph[t[0]].append(t[1])
        for x in graph:
            graph[x].sort()
            graph[x].reverse()
        res = []
        self.dfs(graph, 'JFK', res)
        return res[::-1]

    def dfs(self, graph, start, res):
        while start in graph and graph[start]:
            self.dfs(graph, graph.pop(), res)
        res.append(start)
