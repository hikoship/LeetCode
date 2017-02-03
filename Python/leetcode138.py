# Copy List with Random Pointer

# two loops. store newly created nodes in hashmap

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        nodeMap = {}
        newHead = None
        flag = True
        n1 = head
        n2 = newHead
        while n1:
            # WRONG: n2 = RandomListNode()
            n2 = RandomListNode(n1.label)
            if flag:
                newHead = n2
                flag = False
            nodeMap[n2.label] = n2
            n1 = n1.next
            n2 = n2.next
        n1 = head
        n2 = newHead
        while n1:
            # WRONG: forget if n1.next and if n1.random
            if n1.next:
                n2.next = nodeMap[n1.next.label]
            if n1.random:
                n2.random = nodeMap[n1.random.label]
            n1 = n1.next
            n2 = n2.next
        return newHead
