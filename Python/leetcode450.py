# Delete Node in a BST

# recursion; if right is null, return left; else, put leftmost child of right subtree as new root

# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
#
# Basically, the deletion can be divided into two stages:
#
# Search for a node to remove.
# If the node is found, delete the node.
# Note: Time complexity should be O(height of tree).
#
# Example:
#
# root = [5,3,6,2,4,null,7]
# key = 3
#
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Given key to delete is 3. So we find the node with value 3 and delete it.
#
# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
#
#     5
#    / \
#   4   6
#  /     \
# 2       7
#
# Another valid answer is [5,2,6,null,4,null,7].
#
#     5
#    / \
#   2   6
#    \   \
#     4   7
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        if root.right:
            if root.right.left is None:
                root.right.left = root.left
                return root.right
            node = root.right
            while node.left.left:
                node = node.left
            newRoot = node.left
            # BUG: node.left = None
            node.left = newRoot.right
            newRoot.left = root.left
            newRoot.right = root.right
            return newRoot
        return root.left

# slow but doesn't change node's value; work for bt
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return root
        if root.val != key:
            root.left = self.deleteNode(root.left, key)
            root.right = self.deleteNode(root.right, key)
            return root
        if root.right:
            if root.right.left is None:
                root.right.left = root.left
                return root.right
            node = root.right
            while node.left.left:
                node = node.left
            newRoot = node.left
            # BUG: node.left = None
            node.left = newRoot.right
            newRoot.left = root.left
            newRoot.right = root.right
            return newRoot
        return root.left


# wrong. only works for bt
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return root
        if root.val != key:
            root.left = self.deleteNode(root.left, key)
            root.right = self.deleteNode(root.right, key)
            return root
        if root.right:
            newRoot = root.right
            tmp = TreeNode(newRoot.val)
            tmp.left = newRoot.left
            tmp.right = newRoot.right
            newRoot.left = root.left
            newRoot.right = self.deleteNode(tmp, tmp.val)
            return newRoot
        elif root.left:
            newRoot = root.left
            tmp = TreeNode(newRoot.val)
            tmp.left = newRoot.left
            tmp.right = newRoot.right
            newRoot.left = self.deleteNode(tmp, tmp.val)
            newRoot.right = root.right
            return newRoot
        return None
