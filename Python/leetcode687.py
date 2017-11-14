# Longest Univalue Path

# same as lc124, lc298

# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
#
# Note: The length of path between two nodes is represented by the number of edges between them.
#
# Example 1:
#
# Input:
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output:
#
# 2
# Example 2:
#
# Input:
#
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output:
#
# 2
# Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = 0


    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.helper(root)
        return self.res - 1


    def helper(self, root):
        # BUG: Very big bug. The code will not run through helper if root.left.val != root.val
        # left = self.helper(root.left) if root.left and root.left.val == root.val else 0
        # right = self.helper(root.right) if root.right and root.right.val == root.val else 0
        left = self.helper(root.left) if root.left else 0
        right = self.helper(root.right) if root.right else 0
        # BUG: if root.left.val != root.val:
        if root.left and root.left.val != root.val:
            left = 0
        if root.right and root.right.val != root.val:
            right = 0
        res = max(left, right) + 1
        self.res = max(self.res, res, left + right + 1)
        return res
