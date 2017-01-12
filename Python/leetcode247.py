# Strobogrammatic Number II

# two methods: top-down and bottom-up. Be careful with 0

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
# Find all strobogrammatic numbers that are of length = n.
#
# For example,
# Given n = 2, return ["11","69","88","96"].
#
# Hint:
#
# Try to use recursion and notice that it should recurse with n - 2 instead of n - 1.

# Bottom-up
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.f(n, True)

    def f(self, n, isFirst):
        if n == 0:
            return ['']
        elif n == 1:
            return ['0', '1', '8']
        prevRes = self.f(n - 2, False)
        res = []
        for num in prevRes:
            # WRONG: if isFirst:
            if not isFirst:
                res.append('0' + num + '0') # "00" is not valid
            res.append('1' + num + '1')
            res.append('6' + num + '9')
            res.append('8' + num + '8')
            res.append('9' + num + '6')
        return res


# Top-down
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.f("", n, res)
        return res

    def f(self, prefix, n, res):
        if n == 0:
            res.append(prefix + self.rotate(prefix))
            return
        if n == 1:
            # WRONG: for c in '01689':
            for c in '018':
                res.append(prefix + c + self.rotate(prefix))
            return
        else:
            for c in '01689':
                if prefix != '' or c != '0': # "00" is not valid
                    # WRONG: self.f(prefix + 'c', n - 2, res)
                    self.f(prefix + c, n - 2, res)

    def rotate(self, s):
        tmp = ""
        for c in s:
            if c == '0':
                tmp = '0' + tmp
            elif c == '1':
                tmp = '1' + tmp
            elif c == '6':
                tmp = '9' + tmp
            elif c == '8':
                tmp = '8' + tmp
            elif c == '9':
                tmp = '6' + tmp
        return tmp
