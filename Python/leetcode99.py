# Recover Binary Search Tree

# inorder traversal.
# The first invalid element is larger than its successor;
# the second is smaller than its predecessor

# Two elements of a binary search tree (BST) are swapped by mistake.
#
# Recover the tree without changing its structure.
#
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# recursive O(logn) space:
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        nodes = [TreeNode(float('-inf')), None, None]
        self.helper(nodes, root) # WRONG: HOW I COULD OMIT THIS?
        nodes[1].val, nodes[2].val = nodes[2].val, nodes[1].val

    def helper(self, nodes, root):
        if root is None:
            return
        self.helper(nodes, root.left)
        # For inorder traversal, this piece of codes is executed in the increasing order of node.val
        if nodes[0].val > root.val:
            if nodes[1] is None:
                nodes[1] = nodes[0]
            nodes[2] = root
        nodes[0] = root
        self.helper(nodes, root.right)




# O(n) space: in-order traverse; swap; rebuild tree
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        res = []
        self.helper(res, root)
        first= -1
        for i in range(len(res) - 1):
            if res[i].val > res[i + 1].val:
                first = i
        second = first + 1
        for i in range(first + 1, len(res) - 1):
            if res[i].val > res[i + 1].val:
                second = i + 1
        res[first].val, res[second].val = res[second].val, res[first].val



    def helper(self, res, root):
        if root is None:
            return
        self.helper(res, root.left)
        res.append(root)
        self.helper(res, root.right)

# wrong?
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root, float('-inf'), float('inf'))

    def helper(self, root, minVal, maxVal):
        if root is None:
            return None
        swapRoot = False
        if root.val < minVal or root.val > maxVal:
            swapRoot = True
        left = self.helper(root.left, minVal, root.val)
        right = self.helper(root.right, root.val, maxVal)
        if left and right:
            left.val, right.val = right.val, left.val
            return None
        if swapRoot and left:
            root.val, left.val = left.val, root.val
            return None
        if swapRoot and right:
            root.val, right.val = right.val, root.val
            return None
        if swapRoot:
            return swapRoot
        if left:
            return left
        return right
