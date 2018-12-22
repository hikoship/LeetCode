class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        self.dfs(num, target, res, start, prev)
        return res


    def dfs(self, s, target, res, start, prev):
        if start == len(s):
            if prev[-1] == '+' and eval(''.join(prev)[:-1] == target):
                res.append(''.join(prev))
            return
        for i in range(start, len(s)):
            prev.append(s[start : i + 1])
            # add
            prev.append('+')
            self.dfs(s, target, res, i + 1, prev)
            prev.pop()
            # subtract
            prev.append('-')
            self.dfs(s, target, res, i + 1, prev)
            prev.pop()
            # multiply
            prev.append('*')
            self.dfs(s, target, res, i + 1, prev)
            prev.pop()
            prev.pop()
