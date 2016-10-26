# House Robber III

# DP: store results with tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# TLE
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res = root.val
        if root.left:
            res += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            res += self.rob(root.right.left) + self.rob(root.right.right)
        return max(res, self.rob(root.left) + self.rob(root.right))

# store with array: MLE
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        h = self.getHeight(root)
        store = [-1] * (2 ** h)
        return self.f(root, store, 1)

    def getHeight(self, root):
        if root is None:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def f(self, root, store, loc):
        if root is None:
            return 0
        if store[loc] > -1:
            return store[loc]
        res = root.val
        if root.left:
            res += self.f(root.left.left, store, loc * 4) + self.f(root.left.right, store, loc * 4 + 1)
        if root.right:
            res += self.f(root.right.left, store, loc * 4 + 2) + self.f(root.right.right, store, loc * 4 + 3)
        res = max(res, self.f(root.left, store, loc * 2) + self.f(root.right, store, loc * 2 + 1))
        store[loc] = res
        return res

# store with tree
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        store = self.initStore(root)
        return self.f(root, store)

    def initStore(self, root):
        if root is None:
            return
        node = TreeNode(0)
        node.left = self.initStore(root.left)
        node.right = self.initStore(root.right)
        return node

    def f(self, root, store):
        if root is None:
            return 0
        if store.val > 0:
            return store.val
        res = root.val
        if root.left:
            res += self.f(root.left.left, store.left.left) + self.f(root.left.right, store.left.right)
        if root.right:
            res += self.f(root.right.left, store.right.left) + self.f(root.right.right, store.right.right)
        res = max(res, self.f(root.left, store.left) + self.f(root.right, store.right))
        store.val = res
        return res
