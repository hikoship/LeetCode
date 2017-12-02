# Evaluate Division

# graph dfs

# Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.
#
# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].
#
# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.
#
# According to the example above:
#
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
# The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

# amazingly fast (beats 97%)
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = {}
        for (s, t), v in zip(equations, values):
            if s not in graph:
                graph[s] = []
            if t not in graph:
                graph[t] = []
            graph[s].append((t, v))
            graph[t].append((s, 1.0 / v))
        res = []
        for s, t in queries:
            res.append(self.dfs(graph, s, t, set()))
        return res

    def dfs(self, graph, s, t, visited):
        if s in visited:
            return -1.0
        if s not in graph:
            return -1.0
        if s == t:
            return 1.0
        visited.add(s)
        res = -1.0
        for e, v in graph[s]:
            res = self.dfs(graph, e, t, visited)
            if res != -1.0:
                res = v * res
                break
        visited.remove(s)
        return res



# using cache is not as easy as it seems due to cycle. slow
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
