# Number of Islands II

# union-find

# A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example:
#
# Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).
#
# 0 0 0
# 0 0 0
# 0 0 0
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
#
# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
#
# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
#
# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
#
# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# We return the result as an array: [1, 1, 2, 3]
#
# Challenge:
#
# Can you do it in time complexity O(k log mn), where k is the length of the positions?


# simplified initialization
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parent = {}
        size = {}
        lands = set()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        count = 0
        res = []
        for p in positions:
            count += 1
            p = tuple(p)
            lands.add(p)
            parent[p] = p
            size[p] = 1
            for d in dirs:
                neighbor = (p[0] + d[0], p[1] + d[1])
                if neighbor in lands:
                    count -= self.union(parent, size, p, neighbor)
            res.append(count)
        return res


    def root(self, parent, p):
        if p!= parent[p]:
            parent[p] = self.root(parent, parent[p])
        return parent[p]


    def union(self, parent, size, p1, p2):
        x = self.root(parent, p1)
        y = self.root(parent, p2)
        if x == y:
            return 0
        if size[x] < size[y]:
            parent[x] = y
            size[y] += size[x]
        else:
            parent[y] = x
            size[x] += size[y]
        return 1



# updated counting algorithm. passed but slow
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parent = {}
        size = {}
        isLand = {}
        for i in range(m):
            for j in range(n):
                parent[(i, j)] = (i, j)
                size[(i, j)] = 1
                isLand[(i, j)] = False

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        count = 0
        res = []
        for p in positions:
            count += 1
            p = tuple(p)
            isLand[p] = True
            for d in dirs:
                neighbor = (p[0] + d[0], p[1] + d[1])
                # WRONG: if isLand[neighbor]:
                if neighbor in isLand and isLand[neighbor]:
                    count -= self.union(parent, size, p, neighbor)
            res.append(count)
        return res


    def root(self, parent, p):
        if p!= parent[p]:
            parent[p] = self.root(parent, parent[p])
        return parent[p]


    def union(self, parent, size, p1, p2):
        x = self.root(parent, p1)
        y = self.root(parent, p2)
        if x == y:
            return 0
        if size[x] < size[y]:
            parent[x] = y
            size[y] += size[x]
        else:
            parent[y] = x
            size[x] += size[y]
        return 1










# TLE for 100 * 100 grid
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parent = {}
        size = {}
        isLand = {}
        for i in range(m):
            for j in range(n):
                parent[(i, j)] = (i, j)
                size[(i, j)] = 1
                isLand[(i, j)] = False

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = []
        for p in positions:
            p = tuple(p)
            isLand[p] = True
            for d in dirs:
                neighbor = (p[0] + d[0], p[1] + d[1])
                # WRONG: if isLand[neighbor]:
                if neighbor in isLand and isLand[neighbor]:
                    self.union(parent, size, p, neighbor)
            roots = set()
            for p in parent:
                root = self.root(parent, p)
                if isLand[p] and not root in roots:
                    roots.add(root)
            res.append(len(roots))
        return res


    def root(self, parent, p):
        if p!= parent[p]:
            parent[p] = self.root(parent, parent[p])
        return parent[p]


    def union(self, parent, size, p1, p2):
        x = self.root(parent, p1)
        y = self.root(parent, p2)
        if x == y:
            return
        if size[x] < size[y]:
            parent[x] = y
            size[y] += size[x]
        else:
            parent[y] = x
            size[x] += size[y]
        return
