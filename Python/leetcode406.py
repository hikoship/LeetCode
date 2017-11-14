# Queue Reconstruction by Height

# insertion sort

# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
#
# Note:
# The number of people is less than 1,100.
#
#
# Example
#
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

# insertion sort
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda p: (-p[0], p[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res



# TLE
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        origin = [[x[0], x[1]] for x in people]
        for i in range(len(people)):
            minHeight =     1 << 31 - 1
            idx = -1;
            for j in range(len(people)):
                if people[j][1] == 0 and people[j][0] < minHeight:
                    idx = j
                    minHeight = people[j][0]
            res.append(origin[idx])
            people[idx][1] = -1
            for j in range(len(people)):
                if people[j][0] <= minHeight:
                    people[j][1] -= 1
        return res
