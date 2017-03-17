# Walls and Gates

# BFS; the first layer are the gates

# You are given a m x n 2D grid initialized with these three possible values.
#
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
#
# For example, given the 2D grid:
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if rooms == []:
            return
        prev = []
        # WRONG: di = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
        di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        M = len(rooms)
        N = len(rooms[0])
        visited = [[False] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if rooms[i][j] == 0:
                    prev.append([i, j])
        cur = []
        dis = 1
        while prev:
            for point in prev:
                x = point[0]
                y = point[1]
                for d in di:
                    p = x + d[0]
                    q = y + d[1]
                    if 0 <= p < M and 0 <= q < N and rooms[p][q] > 0 and not visited[p][q]:
                        # WRONG: rooms[x][y] = min(rooms[x][y], dis)
                        rooms[p][q] = min(rooms[p][q], dis)
                        cur.append([p, q])
                        visited[p][q] = True
            dis += 1
            prev = cur
            cur = []



# TLE
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if rooms == []:
            return
        gates = []
        # WRONG: di = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
        di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        M = len(rooms)
        N = len(rooms[0])
        for i in range(M):
            for j in range(N):
                if rooms[i][j] == 0:
                    gates.append([i, j])
        for g in gates:
            visited = [[False] * N for _ in range(M)]
            cur = []
            prev = [g]
            dis = 1
            while prev:
                for point in prev:
                    x = point[0]
                    y = point[1]
                    for d in di:
                        p = x + d[0]
                        q = y + d[1]
                        if 0 <= p < M and 0 <= q < N and rooms[p][q] > 0 and not visited[p][q]:
                            # WRONG: rooms[x][y] = min(rooms[x][y], dis)
                            rooms[p][q] = min(rooms[p][q], dis)
                            cur.append([p, q])
                            visited[p][q] = True
                dis += 1
                prev = cur
                cur = []
