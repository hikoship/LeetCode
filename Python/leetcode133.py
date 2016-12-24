# Clone Graph

# dfs + map. cannot understand it very clearly.. sigh

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        visited = {}
        return self.f(node, visited)

    def f(self, node, visited):
        if node.label in visited:
            return visited[node.label]
        newNode = UndirectedGraphNode(node.label)
        visited[node.label] = newNode
        for neighbor in node.neighbors:
            newNode.neighbors.append(self.f(neighbor, visited))
        return newNode
