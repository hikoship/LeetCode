# Friend Circles

# dfs / union find

# There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.
#
# Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.
#
# Example 1:
# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
# The 2nd student himself is in a friend circle. So return 2.
# Example 2:
# Input:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
# Note:
# N is in range [1,200].
# M[i][i] = 1 for all students.
# If M[i][j] = 1, then M[j][i] = 1.

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        visited = [False] * N
        res = 0
        for i in range(N):
            if visited[i]:
                continue
            stack = [i]
            visited[i] = True
            while stack:
                x = stack.pop()
                # WRONG: for y in M[x]:
                for y in range(N):
                    # WRONG: if not visited[y]:
                    if not visited[y] and M[x][y] == 1:
                        visited[y] = True
                        stack.append(y)
            res += 1
        return res

# wrong union-find ???
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        parent = range(N)
        size = [1] * N
        for i in range(N):
            for j in range(i + 1, N):
                if M[i][j] == 1:
                    self.union(parent, size, i, j)
        s = set()
        for i in range(N):
            s.add(parent[i])
        return len(s)



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
        return


    def root(self, parent, i):
        if i != parent[i]:
            parent[i] = self.root(parent, parent[i])
        return parent[i]
