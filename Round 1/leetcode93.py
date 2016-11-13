# Restore IP Addresses

# dfs. lazy to pass index

# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# For example:
# Given "25525511135",
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

class Solution(object):
    def __init__(self):
        self.res = []

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.f(s, [])
        return self.res

    def f(self, s, prev):
        if len(s) == 0:
            return
        if len(prev) == 3:
            if len(s) == 1 or len(s) <=3 and s[0] != '0' and int(s) <= 255:
                self.res.append('.'.join(prev) + '.' + s)
            return
        self.f(s[1:], prev + [s[:1]])
        if s[0] != '0':
            self.f(s[2:], prev + [s[:2]])
            if 100 <= int(s[:3]) <= 255:
                self.f(s[3:], prev + [s[:3]])
