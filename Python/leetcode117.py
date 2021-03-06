# Populating Next Right Pointers in Each Node II

# Queue

# Follow up for problem "Populating Next Right Pointers in Each Node".
#
# What if the given tree could be any binary tree? Would your previous solution still work?
#
# Note:
#
# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        from Queue import Queue
        if root is None:
            return
        nodes = Queue()
        nodes.put(root)
        nodes.put(None)
        while True:
            tmp = nodes.get()
            if tmp is None:
                return
            while tmp:
                if tmp.left:
                    nodes.put(tmp.left)
                if tmp.right:
                    nodes.put(tmp.right)
                tmp.next = nodes.get()
                tmp = tmp.next
            nodes.put(None)
        return
