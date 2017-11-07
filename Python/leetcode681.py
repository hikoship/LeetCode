# Next Closest Time

# scan from right to left; change to next larger number; check validation; if invalid, change to smallest number

# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.
#
# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
#
# Example 1:
#
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
# Example 2:
#
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        t = map(lambda x: int(x), [time[0], time[1], time[3], time[4]])
        values = sorted(list(set(t)), reverse=True) # numbers in descending order
        indices = {} # indices of numbers in descending order
        for (i, x) in enumerate(values):
            indices[x] = i

        for i in range(3, -1, -1):
            index = indices[t[i]]
            if index > 0:
                # t[i] is not the largest number
                t[i] = values[index - 1]
                if t[0] * 10 + t[1] < 24 and t[2] * 10 + t[3] < 60:
                    # t is valid
                    break
            t[i] = values[-1] # change to smallest number
        return '%d%d:%d%d' % (t[0], t[1], t[2], t[3])
