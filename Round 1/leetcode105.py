# Construct Binary Tree from Preorder and Inorder Traversal

# pass index

# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# MLE
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        l = len(preorder)
        if l == 0:
            return None
        root = TreeNode(preorder[0])
        locRoot = inorder.index(root.val)
        # lenLeft = locRoot
        # lenRight = l - locRoot - 1
        root.left = self.buildTree(preorder[1 : locRoot + 1], inorder[:locRoot])
        root.right = self.buildTree(preorder[locRoot + 1: ], inorder[locRoot + 1:])
        return root

# pass index
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        l = len(preorder)
        return self.f(preorder, inorder, 0, l - 1, 0, l - 1)

    def f(self, preorder, inorder, preStart, preEnd, inStart, inEnd):
        if preStart > preEnd:
            return None
        root = TreeNode(preorder[preStart])
        locRoot = inorder.index(root.val)
        lenLeft = locRoot - inStart
        lenRight = inEnd - locRoot
        root.left = self.f(preorder, inorder, preStart + 1, preStart + lenLeft, inStart, inStart + lenLeft - 1)
        root.right = self.f(preorder, inorder, preEnd - lenRight + 1, preEnd, inEnd - lenRight + 1, inEnd)
        return root
