# Find Largest Value in Each Tree Row

# level order traversal

# You need to find the largest value in each row of a binary tree.
# 
# Example:
# Input: 
# 
#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 
# 
# Output: [1, 3, 9]

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        cur = [root]
        prev = []
        while cur:
            # WRONG: res.append(max(cur, key=lambda x: x.val))
            res.append(max(cur, key=lambda x: x.val).val)
            prev = cur
            cur = []
            for node in prev:
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
        return res
