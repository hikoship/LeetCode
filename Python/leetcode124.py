# Binary Tree Maximum Path Sum

# M1. return two values; M2. update global maximum

# Given a binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
#
# For example:
# Given the below binary tree,
#
#        1
#       / \
#      2   3
# Return 6.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# my solution: return two values. One is max path sum that root is one end; The other has no this restrict
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return max(self.helper(root))


    def helper(self, root):
        if root is None:
            return float('-inf'), float('-inf')
        leftEnd, left = self.helper(root.left)
        rightEnd, right = self.helper(root.right)
        rootEnd = max(leftEnd, rightEnd, 0) + root.val
        return rootEnd, max(rootEnd, left, right, leftEnd + rightEnd + root.val)


# use a global var to store max value
class Solution(object):
    def __init__(self):
        self.res = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.helper(root)
        return self.res


    def helper(self, root):
        if root is None:
            return float('-inf')
        left = self.helper(root.left)
        right = self.helper(root.right)
        res = max(left, right, 0) + root.val
        # WRONG: self.res = max(self.res, res)
        self.res = max(self.res, res, left + right + root.val)
        return res
