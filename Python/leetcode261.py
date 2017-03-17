# Graph Valid Tree

# DFS or union-find

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
#
# For example:
#
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
#
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
#
# Hint:
#
# Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? Is this case a valid tree?
# According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# DFS
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False
        if n == 1:
            return True
        graph = {i: set() for i in range(n)}
        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        stack = [edges[0][0]]
        visited = set([edges[0][0]])
        # WRONG: graph[edges[0][1]].remove(edges[0][0])
        while stack:
            node = stack.pop()
            for x in graph[node]:
                if x in visited:
                    return False
                visited.add(x)
                stack.append(x)
                graph[x].remove(node)
        return len(visited) == n




# union-find
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False
        parent = range(n)
        size = [0] * n
        for e in edges:
            self.union(parent, size, e[0], e[1])
        # WRONG
        # for x in parent:
        #     if x != parent[0]:
        #         return False
        r = self.root(parent, 0)
        for i in range(1, n):
            if self.root(parent, i) != r:
                return False
        return True


    def union(self, parent, size, p, q):
        x = self.root(parent, p)
        y = self.root(parent, q)
        if x == y:
            return
        if size[x] < size[y]:
            parent[x] = y
            size[y] += size[x]
        else:
            parent[y] = x
            size[x] += size[y]

    def root(self, parent, x):
        if x != parent[x]:
            parent[x] = self.root(parent, parent[x])
        return parent[x]
