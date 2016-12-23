# Sum of Left Leaves

#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        s = 0
        if root.left is not None:
            s += self.f(root.left, 'left')
        if root.right is not None:
            s += self.f(root.right, 'right')
        return s

    def f(self, node, pos):
        if node.left is None and node.right is None:
            if pos == 'left':
                return node.val
            else:
                return 0
        s = 0
        if node.left is not None:
            s += self.f(node.left, 'left')
        if node.right is not None:
            s += self.f(node.right, 'right')
        return s
