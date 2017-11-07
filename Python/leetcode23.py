# Merge k Sorted Lists

# heap

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# no need no create new nodes
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        h = []
        resPtr = ListNode(0)
        cur = resPtr
        for l in lists:
            if l:
                h.append((l.val, l))
        heapq.heapify(h)
        while h:
            cur.next = heapq.heappop(h)[1]
            cur = cur.next
            if cur.next:
                heapq.heappush(h, (cur.next.val, cur.next))
        return resPtr.next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        res = ListNode(0)
        p = res
        for l in lists:
            if l:
                heapq.heappush(h, [l.val, l.next])
        while h:
            e = heapq.heappop(h)
            p.next = ListNode(e[0])
            p = p.next
            if e[1]:
                heapq.heappush(h, [e[1].val, e[1].next])
        return res.next
