# Balanced Binary Tree

# return -1 if subtree is not balanced. only traverse once

# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.depth(root) != -1

    def depth(self, root):
        if root is None:
            return 0
        lh = self.depth(root.left)
        rh = self.depth(root.right)
        if lh == -1 or rh == -1 or abs(lh - rh) > 1:
            return - 1
        return max(lh, rh) + 1
