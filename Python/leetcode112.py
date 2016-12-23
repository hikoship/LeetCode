# Path Sum

# BFS. Use two list to record current level and previous level.

# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        nums = [root.val]
        nodes = [root]
        while len(nodes):
            tmpNodes = []
            tmpNums = []
            for node, num in nodes, nums:
                if node.left is not None:
                    tmpNodes.append(node.left)
                    tmpNums.append(num * 10 + node.left.val)

                if node.right is not None:
                    tmpNodes.append(node.right)
                    tmpNums.append(num * 10 + node.right.val)

                if node.left if None and node.right is None:
                    res += num
            nodes = tmpNodes
            nums = tmpNums
        return res

# recursive
class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}

    # 1. negative weights
    # 2. the terminal node must be a leaf
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            if root.val == sum:
                return True
            else:
                return False
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
