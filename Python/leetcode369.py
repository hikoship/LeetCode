# Plus One Linked List

# two pointers O(n) + O(1)

# Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of the list.
#
# Example:
# Input:
# 1->2->3
#
# Output:
# 1->2->4

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(n) time + O(1) space two-pointer solution by @ocean
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = ListNode(0)
        newHead.next = head
        p1 = newHead
        p2 = head
        while p2:
            if p2.val < 9:
                p1 = p2
            p2 = p2.next
        # all nodes following p1 are 9
        p1.val += 1
        p2 = p1.next
        while p2:
            p2.val = 0
            p2 = p2.next
        return head if newHead.val == 0 else newHead


# my fast O(n) time + O(n) space solution
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        p = head
        while p:
            stack.append(p)
            p = p.next
        while stack:
            p = stack.pop()
            if p.val < 9:
                p.val += 1
                return head
            p.val = 0
        n = ListNode(1)
        n.next = head
        return n

# recursive
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if self.carry(head):
            n = ListNode(1)
            n.next = head
            return n
        else:
            return head

    def carry(self, head):
        if head.next is None or self.carry(head.next):
            if head.val < 9:
                head.val += 1
                return False
            else:
                head.val = 0
                return True
        return False
