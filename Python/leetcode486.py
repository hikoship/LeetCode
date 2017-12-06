# Predict the Winner

# dp
# dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

# Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.
#
# Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.
#
# Example 1:
# Input: [1, 5, 2]
# Output: False
# Explanation: Initially, player 1 can choose between 1 and 2.
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
# Hence, player 1 will never be the winner and you need to return False.
# Example 2:
# Input: [1, 5, 233, 7]
# Output: True
# Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
# Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
# Note:
# 1 <= length of the array <= 20.
# Any scores in the given array are non-negative integers and will not exceed 10,000,000.
# If the scores of both players are equal, then player 1 is still the winner.


# dp
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        dp = [[0] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = nums[i]
        for i in range(N - 2, -1, -1):
            for j in range(i + 1, N):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        # BUG: return dp[N - 1][N - 1] >= 0
        return dp[0][N - 1] >= 0


# memorization
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cache = {}
        return self.score(nums, 0, len(nums) - 1, cache) >= 0

    def score(self, nums, i, j, cache):
        if i > j:
            return 0
        if (i, j) not in cache:
            cache[(i, j)] = max(nums[i] - self.score(nums, i + 1, j, cache), nums[j] - self.score(nums, i, j - 1, cache))
        return cache[(i, j)]
