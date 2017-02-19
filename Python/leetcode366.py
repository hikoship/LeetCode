# Find Leaves of Binary Tree

# Recursion and return level

# Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.
#
# Example:
# Given binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Returns [4, 5, 3], [2], [1].
#
# Explanation:
# 1. Removing the leaves [4, 5, 3] would result in this tree:
#
#           1
#          /
#         2
# 2. Now removing the leaf [2] would result in this tree:
#
#           1
# 3. Now removing the leaf [1] would result in the empty tree:
#
#           []
# Returns [4, 5, 3], [2], [1].
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.f(root, res)
        return res

    def f(self, root, res):
        if root is None:
            return 0
        slot = max(self.f(root.left, res), self.f(root.right, res))
        if slot >= len(res):
            res.append([root.val])
        else:
            res[slot].append(root.val)
        return slot + 1
