# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = 0

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.isUnival(root)
        return self.res

    def isUnival(self, root):
        if root is None:
            return True

        # WRONG:
        # if self.isUnival(root.left) and self.isUnival(root.right) and (root.left is None or root.val == root.left.val) and (root.right is None or root.val == root.right.val):
        
        b1 = self.isUnival(root.left)
        b2 = self.isUnival(root.right)

        if b1 and b2 and (root.left is None or root.val == root.left.val) and (root.right is None or root.val == root.right.val):
            self.res += 1
            return True
        return False
