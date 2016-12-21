# Reorder List

# count, reverse, merge

# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# You must do this in-place without altering the nodes' values.
# 
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        # count
        count = 0
        p = ListNode(0)
        p.next = head
        while p.next:
            count += 1
            p.next = p.next.next
        
        # split
        p.next = head
        for i in range((count - 1) / 2):
            p.next = p.next.next
        tmp = ListNode(0)
        tmp.next = p.next.next
        p.next.next = None

        # reverse the second sublist
        newHead = ListNode(0)
        newHead.next = tmp.next
        while tmp.next.next:
            p.next = tmp.next.next
            tmp.next.next = p.next.next
            p.next.next = newHead.next
            newHead.next = p.next
            
           
        # merge head and newHead
        p.next = head
        while newHead.next:
            tmp.next = p.next.next
            p.next.next = newHead.next
            p.next = tmp.next
            tmp.next = newHead.next.next
            newHead.next.next = p.next
            newHead.next = tmp.next