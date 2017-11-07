# Convert BST to Greater Tree

# new value = value from root + value from right subtree; return total value of the tree

# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
#
# Example:
#
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
#
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root, 0)
        return root

    def helper(self, root, value):
        if root is None:
            return 0
        right = self.helper(root.right, value)
        left = self.helper(root.left, value + root.val + right)
        tmp = root.val
        root.val += value + right
        return tmp + left + right
