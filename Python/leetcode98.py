# Validate Binary Search Tree

# recursion: pass the min and max possible value of subtree

# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#     2
#    / \
#   1   3
# Binary tree [2,1,3], return true.
# Example 2:
#     1
#    / \
#   2   3
# Binary tree [1,2,3], return false.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# pass min and max value
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.f(root, -2 ** 31 - 1, 2 ** 31)

    def f(self, root, minVal, maxVal):
        if root is None:
            return True
        if root.val <= minVal or root.val >= maxVal:
            return False
        return self.f(root.left, minVal, root.val) and self.f(root.right, root.val, maxVal)

# inorder traversal
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        return self.f(root, res)

    def f(self, root, res):
        if root is None:
            return True
        if not self.f(root.left, res):
            return False
        if res != [] and root.val <= res[-1]:
            return False
        res.append(root.val)
        rightMin = len(res)
        if not self.f(root.right, res):
            return False
        if len(res) > rightMin and root.val >= res[rightMin]:
            return False
        return True


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        self.f(root, res)
        for i in range(1, len(res)):
            if res[i] <= res[i - 1]:
                return False
        return True

    def f(self, root, res):
        if root is None:
            return
        self.f(root.left, res)
        res.append(root.val)
        self.f(root.right, res)
