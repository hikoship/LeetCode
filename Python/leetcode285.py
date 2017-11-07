# Inorder Successor in BST

# inorder traversal or recursive

# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iterative, if no duplicates
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        cur = root
        res = None
        while cur:
            if p.val >= cur.val:
                cur = cur.right
            else:
                res = cur
                cur = cur.left
        return res

# recursive, if no duplicates
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)
        left = self.inorderSuccessor(root.left, p)
        return left if left else root



# traversal
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        cur = root
        prev = None
        stack = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            if prev == p:
                return stack.pop()
            prev = stack.pop()
            cur = prev.right
        return None
