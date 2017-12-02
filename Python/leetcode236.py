# Lowest Common Ancestor of a Binary Tree

# If the two targets belong to the left and right sub-tree respectively, then the root is the answer.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right



# Record path: MLE...
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pathP = self.findPath(root, p, '')
        pathQ = self.findPath(root, q, '')
        node = root
        for i in range(min(len(pathP), len(pathQ))):
            if pathP[i] != pathQ[i]:
                break
            node = node.left if pathP[i] == 'l' else node.right
        return node


    def findPath(self, root, target, path):
        if root is None:
            return ''
        if root == target:
            return path
        # WRONG: use same name for res and path
        # path = self.findPath(root.left, target, path + 'l')
        res = self.findPath(root.left, target, path + 'l')
        if res == '':
            res = self.findPath(root.right, target, path + 'r')
        return res
