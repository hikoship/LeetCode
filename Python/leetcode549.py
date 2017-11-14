# Binary Tree Longest Consecutive Sequence II

# for each recursion, return the length of increasing path and decreasing path

# Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.
#
# Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.
#
# Example 1:
# Input:
#         1
#        / \
#       2   3
# Output: 2
# Explanation: The longest consecutive path is [1, 2] or [2, 1].
# Example 2:
# Input:
#         2
#        / \
#       1   3
# Output: 3
# Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
# Note: All the values of tree nodes are in the range of [-1e7, 1e7].


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = 0


    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.helper(root)
        return self.res


    def helper(self, root):
        leftAsc = 0
        leftDesc = 0
        rightAsc = 0
        rightDesc = 0
        # left
        if root.left:
            leftAsc, leftDesc = self.helper(root.left)
            if root.val - root.left.val != 1:
                leftAsc = 0
            if root.left.val - root.val != 1:
                leftDesc = 0
        # right
        if root.right:
            rightAsc, rightDesc = self.helper(root.right)
            if root.val - root.right.val != 1:
                rightAsc = 0
            if root.right.val - root.val != 1:
                rightDesc = 0
        self.res = max(self.res, leftAsc + rightDesc + 1, leftDesc + rightAsc + 1)
        return max(leftAsc, rightAsc) + 1, max(leftDesc, rightDesc) + 1
