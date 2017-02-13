# Swap Nodes in Pairs

# two pointers or recursion

# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# iterative
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        newHead = head.next
        p1, p2 = head, head.next
        while p1 and p2 and p2.next and p2.next.next:
            p1.next = p2.next.next
            tmp = p1
            p1 = p2.next
            p2.next = tmp
            p2 = p1.next
        if p1 and p2:
            p1.next, p2.next = p2.next, p1
        return newHead

# recursive
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(head.next.next)
        newHead.next = head
        return newHead
