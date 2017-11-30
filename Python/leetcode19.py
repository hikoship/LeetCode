# Remove Nth Node From End of List

# two points: y for tail; x for node to be deleted

# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
#
#    Given linked list: 1->2->3->4->5, and n = 2.
#
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        resPtr = ListNode(0)
        resPtr.next = head
        x = resPtr
        y = resPtr
        for i in range(n):
            y = y.next
        while y.next:
            x = x.next
            y = y.next
        # y = tail. delete x.next
        x.next = x.next.next
        return resPtr.next
