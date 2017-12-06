# Closest Binary Search Tree Value II

# inorder + bs + two pointers (see bst, think inorder)

# Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.
#
# Note:
# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        array = self.inorderTraversal(root)
        i = self.binarySearch(array, target)
        j = i + 1
        res = []
        while len(res) < k:
            if j >= len(array) or i >= 0 and abs(array[i] - target) < abs(array[j] - target):
                res.append(array[i])
                i -= 1
            else:
                res.append(array[j])
                j += 1
        return res


    def inorderTraversal(self, root):
        stack, res = [], []
        cur = root
        while True:
            while cur:
                stack.append(cur)
                cur = cur.left
            if not stack:
                return res
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right


    # largest i where array[i] <= target
    def binarySearch(self, array, target):
        low = 0
        high = len(array) - 1
        while low < high:
            mid = low + (high - low + 1) / 2
            if array[mid] <= target:
                low = mid
            else:
                high = mid - 1
        return low
