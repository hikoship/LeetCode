# Increasing Triplet Subsequence

# 我的思路：假设序列为 abc，则记录潜在的 ab 对。扫到的第 i 个数如果比 ab 大，返回真。如果比 a 大比 b 小，更新 ab 为 ai。如果比 a 小，更新 ab 为 ib。

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num1 = 2 ** 31 - 1
        num2 = 2 ** 31 - 1
        for n in nums:
            print n
            if num2 < n:
                return True
            elif num1 < n:
                num2 = n
            else:
                num1 = n
        return False
