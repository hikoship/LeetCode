# Reverse Linked List

# ...what to say

# Reverse a singly linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p1 = head
        p2 = head.next
        while p2:
            head.next = p2.next
            p2.next = p1
            p1 = p2
            p2 = head.next
        return p1

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            newHead = head.next
            head.next = prev
            prev = head
            head = newHead
        return prev

# recursive
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.f(head, None)

    def f(self, head, prev):
        if head is None:
            return prev
        newHead = head.next
        head.next = prev
        return self.f(newHead, head)
