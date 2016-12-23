# Binary Watch

#

# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
#
# Each LED represents a zero or one, with the least significant bit on the right.
#
# https://upload.wikimedia.org/wikipedia/commons/8/8b/Binary_clock_samui_moon.jpg
#
# For example, the above binary watch reads "3:25".
#
# Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

class Solution(object):
    def __init__(self):
        self.res = []

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num > 8:
            return []
        self.dfs(num, 10, '') # 10 LEDs
        print self.res
        output = []
        for e in self.res:
            hour = int(e[:4], 2)
            if hour > 11:
                continue
            minute = int(e[4:], 2)
            if minute > 59:
                continue
            output.append(str(hour) + ':' + '0' * (minute < 10) + str(minute))
        return output

    def dfs(self, n, l, s):
        if n > 0:
            self.dfs(n - 1, l - 1, s + '1')
        else:
            self.res.append(s + '0' * l)
            print 'a' + s + '0' * l
            return

        if l > n:
            self.dfs(n, l - 1, s + '0')
