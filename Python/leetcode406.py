# cannot copy people by a = people[:] because elements of people are also lists

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
