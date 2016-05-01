# Sum Root to Leaf Numbers

# 可循环（DFS）可迭代（BFS）记录之前各层的信息，如果该节点是叶子就保存计算值。

#Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# For example,
#
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
# Return the sum = 12 + 13 = 25.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive without extra variable to store the result
class Solution(object):
    def total(self, node, num):
        if node is None:
            return 0
        num = 10 * num + node.val
        if node.left is None and node.right is None:
            return num
        return self.total(node.left, num) + self.total(node.right, num)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.total(root, 0)

# BFS
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res = 0
        nums = [root.val]
        nodes = [root]
        while len(nodes):
            tmpNodes = []
            tmpNums = []
            for node, num in zip(nodes, nums):
                if node.left is not None:
                    tmpNodes.append(node.left)
                    tmpNums.append(num * 10 + node.left.val)

                if node.right is not None:
                    tmpNodes.append(node.right)
                    tmpNums.append(num * 10 + node.right.val)

                if node.left is None and node.right is None:
                    res += num
            nodes = tmpNodes
            nums = tmpNums
        return res
