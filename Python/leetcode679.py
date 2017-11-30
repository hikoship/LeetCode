# 24 Game

# pick two, calculate all results, and recalculate

# You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.
#
# Example 1:
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
# Example 2:
# Input: [1, 2, 1, 2]
# Output: False
# Note:
# The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
# Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
# You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
#

class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            # BUG: return nums[0] == 24
            return abs(nums[0] - 24) < 0.00001
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                x = nums[i]
                y = nums[j]
                res = [x + y, x - y, y - x, x * y]
                if y != 0:
                    res.append(float(x) / y)
                if x != 0:
                    res.append(float(y) / x)
                tmp = []
                for k in range(len(nums)):
                    if k != i and k != j:
                        tmp.append(nums[k])
                for r in res:
                    if self.judgePoint24(tmp + [r]):
                        return True
        return False




s = Solution()
print s.judgePoint24([3,3,8,8])
