# Shortest Word Distance

# I thought too much... again!

# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.
#
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

# one pointer
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        prev = -1
        res = len(words)
        for i, w in enumerate(words):
            if w == word1 or w == word2:
                if prev >= 0 and w != words[prev]: # only difference from leetcode #245
                    res = min(res, i - prev)
                prev = i
        return res

# two pointers
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p1, p2 = -len(words), len(words) # WRONG: p1 and p2 must have enough distance from 0.
        res = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                p1 = i
            if words[i] == word2:
                p2 = i
            res = min(res, abs(p1 - p2))
        return res



        # left / right method is not applicable
        # left = -1
        # right = len(words)
        # res = right
        # while left < right:
        #     left += 1 # Wrong: move left / right before while loop; otherwise dead loop
        #     # Wrong two async loop
        #     while words[left] != word1:
        #         left += 1
        #     if left >= right:
        #         return min(left - right, res)
        #     res = right - left
        #
        #     right -= 1
        #     while words[right] != word2:
        #         right -= 1
        #     if left >= right:
        #         return min(left - right, res)
        #     res = right - left
        #
        # return min(left - right, res)
