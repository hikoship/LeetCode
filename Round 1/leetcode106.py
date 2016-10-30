# Construct Binary Tree from Inorder and Postorder Traversal

# same as #105

# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        l = len(inorder)
        return self.f(inorder, postorder, 0, l - 1, 0, l - 1)

    def f(self, inorder, postorder, inStart, inEnd, postStart, postEnd):
        if inStart > inEnd:
            return None
        root = TreeNode(postorder[postEnd])
        locRoot = inorder.index(root.val)
        lenLeft = locRoot - inStart
        lenRight = inEnd - locRoot
        root.left = self.f(inorder, postorder, inStart, inStart + lenLeft - 1, postStart, postStart + lenLeft - 1)
        root.right = self.f(inorder, postorder, inEnd - lenRight + 1, inEnd, postEnd - lenRight, postEnd - 1)
        return root
