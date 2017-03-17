# Range Addition

# plus on startIndex and minux on endIndex

# Assume you have an array of length n initialized with all 0's and are given k update operations.
#
# Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.
#
# Return the modified array after all k operations were executed.
#
# Example:
#
# Given:
#
#     length = 5,
#     updates = [
#         [1,  3,  2],
#         [2,  4,  3],
#         [0,  2, -2]
#     ]
#
# Output:
#
#     [-2, 0, 3, 5, 3]
# Explanation:
#
# Initial state:
# [ 0, 0, 0, 0, 0 ]
#
# After applying operation [1, 3, 2]:
# [ 0, 2, 2, 2, 0 ]
#
# After applying operation [2, 4, 3]:
# [ 0, 2, 5, 5, 3 ]
#
# After applying operation [0, 2, -2]:
# [-2, 0, 3, 5, 3 ]
# Hint:
#
# Thinking of using advanced data structures? You are thinking it too complicated.
# For each update operation, do you really need to update all elements between i and j?
# Update only the first and end element is sufficient.
# The optimal time complexity is O(k + n) and uses O(1) extra space.


class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * length
        for u in updates:
            if u[0] <= u[1]:
                # WRONG: res[u[0]] = u[2]
                res[u[0]] += u[2]
                if u[1] < length - 1:
                    # WRONG: res[u[1] + 1] = -u[2]
                    res[u[1] + 1] += -u[2]
        for i in range(1, length):
            res[i] += res[i - 1]
        return res





# brute force: TLE
class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * length
        for u in updates:
            for i in range(u[0], u[1] + 1):
                res[i] += u[2]
        return res
