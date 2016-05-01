# Binary Tree Right Side View

# BFS and record current level and previous level

# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        output = []
        array = [[root], []]
        curArray = 0
        while True:
            if len(array[curArray]) == 0:
                return output
            for node in array[curArray]:
                if node.left:
                    array[1 - curArray].append(node.left)
                if node.right:
                    array[1 - curArray].append(node.right)
            output.append(array[curArray][-1].val)
            array[curArray] = [] # clear current array
            curArray = 1 - curArray # swap two arrays
