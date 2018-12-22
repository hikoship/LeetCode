# The Maze III

# trace the movement so far (cannot trace the last step only. eg. 'llu' < 'lul', but the last step 'u' > 'l')

# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.
#
# Given the ball position, the hole position and the maze, find out how the ball could drop into the hole by moving the shortest distance. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the hole (included). Output the moving directions by using 'u', 'd', 'l' and 'r'. Since there could be several different shortest ways, you should output the lexicographically smallest way. If the ball cannot reach the hole, output "impossible".
#
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The ball and the hole coordinates are represented by row and column indexes.
#
# Example 1
#
# Input 1: a maze represented by a 2D array
#
# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0
#
# Input 2: ball coordinate (rowBall, colBall) = (4, 3)
# Input 3: hole coordinate (rowHole, colHole) = (0, 1)
#
# Output: "lul"
# Explanation: There are two shortest ways for the ball to drop into the hole.
# The first way is left -> up -> left, represented by "lul".
# The second way is up -> left, represented by 'ul'.
# Both ways have shortest distance 6, but the first way is lexicographically smaller because 'l' < 'u'. So the output is "lul".
#
# Example 2
#
# Input 1: a maze represented by a 2D array
#
# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0
#
# Input 2: ball coordinate (rowBall, colBall) = (4, 3)
# Input 3: hole coordinate (rowHole, colHole) = (3, 0)
# Output: "impossible"
# Explanation: The ball cannot reach the hole.
#
# Note:
# There is only one ball and one hole in the maze.
# Both the ball and hole exist on an empty space, and they will not be at the same position initially.
# The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and the width and the height of the maze won't exceed 30.
#


class Solution(object):
    def findShortestWay(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        M = len(maze)
        N = len(maze[0])
        distance = [[float('inf')] * N for _ in range(M)]
        move = [[''] * N for _ in range(M)]
        distance[start[0]][start[1]] = 0
        heap = [(0, start)]
        dirs = {(1, 0): 'd', (0, 1): 'r', (-1, 0): 'u', (0, -1): 'l'}
        while heap:
            p = heapq.heappop(heap)[1]
            if p == destination:
                return move[p[0]][p[1]]
            for d in dirs:
                x = p[0]
                y = p[1]
                # key point: [x, y] != destination
                while 0 <= x + d[0] < M and 0 <= y + d[1] < N and [x, y] != destination and maze[x + d[0]][y + d[1]] == 0:
                    x += d[0]
                    y += d[1]
                if [x, y] == p: # do not skip this
                    continue
                newDistance = distance[p[0]][p[1]] + abs(x - p[0]) + abs(y - p[1])
                # BUG: newMove = dirs[d] + move[p[0]][p[1]]
                newMove = move[p[0]][p[1]] + dirs[d]
                if newDistance < distance[x][y] or newDistance == distance[x][y] and newMove < move[x][y]:
                    distance[x][y] = newDistance
                    move[x][y] = newMove
                    heapq.heappush(heap, (distance[x][y], [x, y]))
        return 'impossible'
