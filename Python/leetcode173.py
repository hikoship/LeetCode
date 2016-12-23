# Binary Search Tree Iterator

#

# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
#
# Calling next() will return the next smallest number in the BST.
#
# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.arr = self.buildArr(root)

        self.i = 0
        self.l = len(self.arr)

    def buildArr(self, node):
        if node is None:
            return []
        else:
            return self.buildArr(node.left) + [node.val] + self.buildArr(node.right)


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < self.l


    def next(self):
        """
        :rtype: int
        """
        self.i += 1
        return self.arr[self.i - 1]



# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
