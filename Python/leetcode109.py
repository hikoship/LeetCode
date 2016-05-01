# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return self.sortedArrayToBST(array)

    def sortedArrayToBST(self, array):
        if array == []:
            return None
        mid = len(array) / 2
        root = TreeNode(array[mid])
        root.left = self.sortedArrayToBST(array[:mid])
        root.right = self.sortedArrayToBST(array[mid + 1:])
        return root
        
