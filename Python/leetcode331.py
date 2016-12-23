# Verify Preorder Serialization of a Binary Tree

#

# One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.
#
#      _9_
#     /   \
#    3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
# For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.
#
# Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.
#
# Each comma separated value in the string must be either an integer or a character '#' representing null pointer.
#
# You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".
#
# Example 1:
# "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Return true
#
# Example 2:
# "1,#"
# Return false
#
# Example 3:
# "9,#,#,1"
# Return false

class Solution(object):
    def __init__(self):
        self.i = 0
        self.nodes = []

    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        self.nodes = preorder.split(',')
        return self.f() and self.i == len(self.nodes) - 1

    def f(self):
        if self.i >= len(self.nodes):
            return False
        if self.nodes[self.i] == '#':
            return True
        self.i += 1
        if self.f():
            self.i += 1
            return self.f()
        return False
