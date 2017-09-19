def hasPath(maze, start, destination):
    row = len(maze)
    col = len(maze[0])
    visited = [[False] * col for _ in maze]
    stack = [start]
    visited[0][0] = True
    while stack:
        point = stack.pop()
        if point == destination:
            return True
        x = point[0]
        y = point[1]
        if x > 0 and not visited[x - 1][y] and maze[x - 1][y] == 0:
            visited[x - 1][y] = True
            stack.append([x - 1, y])
        if x < row - 1 and not visited[x + 1][y] and maze[x + 1][y] == 0:
            visited[x + 1][y] = True
            stack.append([x + 1, y])
        if y > 0 and not visited[x][y - 1] and maze[x][y - 1] == 0:
            visited[x][y - 1] = True
            stack.append([x, y - 1])
        if y < col - 1 and not visited[x][y + 1] and maze[x][y + 1] == 0:
            visited[x][y + 1] = True
            stack.append([x, y + 1])
    return False


print hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
,[0,4]
,[3,2])

# class Solution(object):
#     def hasPath(self, maze, start, destination):
#         """
#         :type maze: List[List[int]]
#         :type start: List[int]
#         :type destination: List[int]
#         :rtype: bool
#         """
#         row = len(maze)
#         col = len(maze[0])
#         visited = [[False] * col for _ in maze]
#         stack = [start]
#         visited[0][0] = True
#         while stack:
#             point = stack.pop()
#             if point == destination:
#                 return True
#             x = point[0]
#             y = point[1]
#             if x > 0 and not visited[x - 1][y] and maze[x - 1][y] == 0:
#                 visited[x - 1][y] = True
#                 stack.append([x - 1, y])
#             if x < row - 1 and not visited[x + 1][y] and maze[x + 1][y] == 0:
#                 visited[x + 1][y] = True
#                 stack.append([x + 1, y])
#             if y > 0 and not visited[x][y - 1] and maze[x][y - 1] == 0:
#                 visited[x][y - 1] = True
#                 stack.append([x, y - 1])
#             if y < col - 1 and not visited[x][y + 1] and maze[x][y + 1] == 0:
#                 visited[x][y + 1] = True
#                 stack.append([x, y + 1])
#         return False
