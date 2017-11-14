# Binary Tree Longest Consecutive Sequence

# maintain global max. similar to lc687

# Given a binary tree, find the length of the longest consecutive sequence path.
#
# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).
#
# For example,
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Longest consecutive sequence path is 3-4-5, so return 3.
#    2
#     \
#      3
#     /
#    2
#   /
#  1
# Longest consecutive sequence path is 2-3,not3-2-1, so return 2.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = 0


    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.helper(root)
        return self.res


    def helper(self, root):
        if root.left:
            left = self.helper(root.left)
        if root.left is None or root.val + 1 != root.left.val:
            left = 0
        if root.right:
            right = self.helper(root.right)
        if root.right is None or root.val + 1 != root.right.val:
            right = 0
        res = max(left, right) + 1
        self.res = max(self.res, res)
        return res
