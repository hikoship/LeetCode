# Binary Tree Level Order Traversal II

# same as lc102

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        queue = collections.deque()
        queue.append(root)
        queue.append(None)
        level = []
        while queue:
            node = queue.popleft()
            if node:
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                res.append(level)
                if not queue:
                    break
                level = []
                queue.append(None)
        res.reverse()
        return res
