class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = {}
        for e, v in zip(equations, values):
            s, t = e
            if s not in graph:
                graph[s] = {}
            if t not in graph:
                graph[t] = {}
            graph[s][t] = v
        res = []
        cache = {}
        for s, t in queries:
            res.append(self.helper(graph, cache, s, t))
        return res


    def helper(self, graph, cache, s, t):
        if (s, t) in cache:
            return cache[(s, t)]
        if s not in graph or t not in graph:
            cache[(s, t)] = -1.0
        elif s == t:
            cache[(s, t)] = 1.0
        # WRONG: this should be moved to the bottom
        # elif len(graph[s]) == 0:
        #     cache[(s, t)] = -1.0
        else:
            for neighbor in graph[s]:
                # WRONG: tmp = self.helper(graph, cache, s, t)
                tmp = self.helper(graph, cache, neighbor, t)
                if tmp > -1:
                    cache[(s, t)] = tmp * graph[s][neighbor]
                    break
            if (s, t) not in cache:
                # WRONG: cache[(s, t)] = 1 / self.helper(graph, cache, t, s)
                # WRONG: cache[(s, t)] = 1 / self.helper(graph, cache, t, neighbor)
                # WRONG: cache[(s, t)] = 1.0 / self.helper(graph, cache, t, neighbor)
                cache[(s, t)] = graph[s][neighbor] / self.helper(graph, cache, t, neighbor)
        cache[[(t, s)]] = cache[(s, t)]
        return cache[(s, t)]
