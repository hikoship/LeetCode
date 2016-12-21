# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# maximum recursion depth exceeded
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        length = 0
        while p:
            p = p.next
            length += 1
        return self.f(head, length)
        
    def f(self, p1, length):
        if length < 2:
            return p1
        p = p1
        for i in range(length / 2 - 1):
            p = p.next
        p2 = p.next
        p.next = None
        p1 = self.f(p1, length / 2)
        p2 = self.f(p2, length - length / 2)

        pseudoHead = ListNode(0)
        cur = pseudoHead
        while p1 and p2:
            if p1.val < p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        cur.next = p1 if p1 else p2
        return pseudoHead.next 