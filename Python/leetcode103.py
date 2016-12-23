# Binary Tree Zigzag Level Order Traversal

#

# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        output = []
        array = [[root], []]
        curArray = 0
        while True:
            if len(array[curArray]) == 0:
                return output
            output.append([])
            for node in array[curArray]:
                if node.left:
                    array[1 - curArray].append(node.left)
                if node.right:
                    array[1 - curArray].append(node.right)
            if curArray == 0:
                for node in array[curArray]:
                    output[-1].append(node.val)
            else:
                for node in array[curArray][::-1]:
                    output[-1].append(node.val)
            array[curArray] = [] # clear current array
            curArray = 1 - curArray # swap two arrays
