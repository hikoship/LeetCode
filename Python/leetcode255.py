# Verify Preorder Sequence in Binary Search Tree

# cannot use method for validate Best

# Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.
#
# You may assume each number in the sequence is unique.
#
# Follow up:
# Could you do it using only constant space complexity?

class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack = []
        low = float('-inf')
        for p in preorder:
            if p <=low:
                return False
            while (stack and p > stack[-1]):
                low = stack.pop()
            stack.append(p)
        return True

# constant space
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        l = 0
        low = float('-inf')
        for p in preorder:
            if p <=low:
                return False
            while (l > 0 and p > preorder[l - 1]):
                l -= 1
                low = preorder[l]
            preorder[l] = p
            l += 1
        return True
