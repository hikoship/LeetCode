# Path Sum III

# sum the path from current to node to its ancestors

# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self.f([], root, sum)

    def f(self, stack, root, sum):
        res = 0
        if root is None:
            return 0
        for i in range(len(stack)):
            stack[i] += root.val
        stack.append(root.val)

        res += stack.count(sum) + self.f(stack, root.left, sum) + self.f(stack, root.right, sum)
        stack.pop()
        for i in range(len(stack)):
            stack[i] -= root.val
        return res
