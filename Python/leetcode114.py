# Flatten Binary Tree to Linked List

# Use recursive approach to find a tail. Link right to left tail; return right tail.

# Given a binary tree, flatten it to a linked list in-place.
#
# For example,
# Given
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
# click to show hints.
#
# Hints:
# If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iterative

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        stack = [root]
        while stack != []:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if node.left:
                tail = node.left
                while tail.right:
                    tail = tail.right
                tail.right = node.right
                node.right = node.left
                node.left = None
        return

# recursive
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.f(root)
        return

    def f(self, node):
        if node.left is None and node.right is None:
                return node
        elif node.left is None:
            return self.f(node.right)
        elif node.right is None:
            node.right = node.left
            node.left = None
            return self.f(node.right)
        else:
            rootTail = self.f(node.right)
            tail = self.f(node.left)
            tail.right = node.right
            node.right = node.left
            node.left = None
            return rootTail
