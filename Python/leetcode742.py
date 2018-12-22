# Closest Leaf in a Binary Tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return None
        path = []
        self.findK(root, k, path)
        path.reverse()
        print path
        x = self.findClosest(root, k, path, 0)[1]
        return x.val

    def findK(self, root, k, path):
        if root is None:
            return None
        if root.val == k:
            return root
        left = self.findK(root.left, k, path)
        if left:
            path.append('l')
            return left
        right = self.findK(root.right, k, path)
        if right:
            path.append('r')
            return right

    def findClosest(self, root, k, path, start):
        if start == len(path):
            return self.findShortest(root, k)
        if path[start] == 'l':
            leftVal, left = self.findClosest(root.left, k, path, start + 1)
            rightVal, right = self.findShortest(root.right, k)
            if leftVal < rightVal + len(path) - start + 1:
                return leftVal, left
            return rightVal + len(path) - start + 1, right
        else:
            leftVal, left = self.findShortest(root.left, k)
            rightVal, right = self.findClosest(root.right, k, path, start + 1)
            if rightVal < leftVal + len(path) - start + 1:
                return rightVal, right
            return leftVal + len(path) - start + 1, left

    def findShortest(self, root, k):
        if root is None:
            return [float('inf'), None]
        if root.left is None and root.right is None:
            return 0, root
        leftDepth, left = self.findShortest(root.left, k)
        rightDepth, right = self.findShortest(root.right, k)
        if leftDepth < rightDepth:
            return leftDepth + 1, left
        return rightDepth + 1, right
