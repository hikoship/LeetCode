# Validate Binary Search Tree

# recursion. get isBST, min value, max value of sub trees

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

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        isBST, minVal, maxVal = self.f(root)
        return isBST

    def f(self, root):
        if root.left is None and root.right is None:
            return True, root.val, root.val
        elif root.left is None:
            isBST, minVal, maxVal = self.f(root.right)
            if isBST and root.val < minVal:
                return True, root.val, maxVal
        elif root.right is None:
            isBST, minVal, maxVal = self.f(root.left)
            if isBST and root.val > maxVal:
                return True, minVal, root.val
        else:
            isBSTL, minValL, maxValL = self.f(root.left)
            isBSTR, minValR, maxValR = self.f(root.right)
            if isBSTL and isBSTR and maxValL < root.val < minValR:
                return True, minValL, maxValR
        return False, 0, 0
