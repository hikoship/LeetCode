# Clone Graph

# dfs + map. cannot understand it very clearly.. sigh


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

# removed visited
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        newNode = UndirectedGraphNode(node.label)
        # WRONG: stack = [(newNode, node)]
        stack = [node]
        created = {newNode.label: newNode}
        while stack:
            # WRONG: new, old = stack.pop()
            old = stack.pop()
            new = created[old.label]
            for oldNeighbor in old.neighbors:
                if oldNeighbor.label in created:
                    newNeighbor = created[oldNeighbor.label]
                else:
                    newNeighbor = UndirectedGraphNode(oldNeighbor.label)
                    created[newNeighbor.label] = newNeighbor
                    stack.append(oldNeighbor)
                new.neighbors.append(newNeighbor)
        return newNode

# my iterative solution
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        newNode = UndirectedGraphNode(node.label)
        # WRONG: stack = [(newNode, node)]
        stack = [(node, newNode)]
        created = {newNode.label: newNode}
        while stack:
            # WRONG: new, old = stack.pop()
            old, new = stack.pop()
            if old.label in visited:
                continue
            visited.add(old.label)
            for oldNeighbor in old.neighbors:
                # must not create duplicated new nodes with same label
                if oldNeighbor.label in created:
                    newNeighbor = created[oldNeighbor.label]
                else:
                    newNeighbor = UndirectedGraphNode(oldNeighbor.label)
                    created[newNeighbor.label] = newNeighbor
                new.neighbors.append(newNeighbor)
                stack.append((oldNeighbor, newNeighbor))
        return newNode





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
