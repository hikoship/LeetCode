class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = {}
        cache = {}
        for (s, t), v in zip(equations, values):
            if s not in graph:
                graph[s] = {}
            if t not in graph:
                graph[t] = {}
            graph[s][t] = v
            cache[(s, t)] = v
            graph[t][s] = 1.0 / v
            cache[(t, s)] = 1.0 / v
        res = []
        for s, t in queries:
            res.append(self.helper(graph, cache, s, t, set()))
        return res


    def helper(self, graph, cache, s, t, visited):
        removeFlag = False
        if (s, t) in cache:
            return cache[(s, t)]
        if s not in graph or t not in graph:
            cache[(s, t)] = -1.0
        elif s == t:
            cache[(s, t)] = 1.0
        else:
            visited.add(s)
            for neighbor in graph[s]:
                if neighbor in visited:
                    removeFlag = True
                    continue
                tmp = self.helper(graph, cache, neighbor, t, visited)
                if tmp > -1:
                    cache[(s, t)] = tmp * graph[s][neighbor]
                    break
            visited.remove(s)
        if (s, t) not in cache:
            cache[(s, t)] = -1.0
        cache[(t, s)] = 1.0 / cache[(s, t)]
        if removeFlag and cache[(s, t)] == -1.0:
            del cache[(s, t)]
            del cache[(t, s)]
            return -1
        return cache[(s, t)]
