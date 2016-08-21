# Count Complete Tree Nodes

# Use bit manipulation to judge the middle node; prevent infinite loop.

# Given a complete binary tree, count the number of nodes.
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        height = 1
        node = root.left
        while node is not None:
            node = node.left
            height += 1
        minNum = 2 ** (height - 1)
        maxNum = 2 ** height - 1

        while maxNum - minNum > 1:
            mid = (minNum + maxNum) / 2
            if self.exist(root, height, mid - 2 ** (height - 1)):
                minNum = mid
            else:
                maxNum = mid - 1
        if minNum == maxNum:
            return minNum
        if self.exist(root, height, maxNum - 2 ** (height - 1)):
            return maxNum
        else:
            return minNum

    def exist(self, root, height, n):
        node = root
        mask = 1 << (height - 2)
        while mask > 0:
            if mask & n:
                if node.right is not None:
                    node = node.right
                else:
                    return False
            else:
                if node.left is not None:
                    node = node.left
                else:
                    return False
            mask >>= 1
        return True
