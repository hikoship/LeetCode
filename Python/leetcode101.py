# Symmetric Tree

# stack for iterative solution

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.f(root.left, root.right)

    def f(self, left, right):
        if left is None or right is None:
            return left is None and right is None # return left is right
        if left.val != right.val:
            return False
        return self.f(left.left, right.right) and self.f(left.right, right.left)

# iterative
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is None or root.right is None:
            return root.left is None and root.right is None # return left is right
        stack = [root.left, root.right]
        while stack:
            if len(stack) % 2:
                return False
            left = stack.pop()
            right = stack.pop()
            if left.val != right.val:
                return False
            if left.left and right.right:
                stack.append(left.left)
                stack.append(right.right)
            else:
                if left.left or right.right:
                    return False
            if left.right and right.left:
                stack.append(left.right)
                stack.append(right.left)
            else:
                if left.right or right.left:
                    return False
        return True
