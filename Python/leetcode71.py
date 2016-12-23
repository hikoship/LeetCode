# Simplify Path

# Use stack. the split() function returns empty elements if the parameter is located at the head or tail of the string

# Given an absolute path for a file (Unix-style), simplify it.
#
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        pathArray = path.split('/')
        # remove empty string
        # [:] means it changes original elements instead of creating a new list
        pathArray[:] = [p for p in pathArray if p != '']
        for p in pathArray:
            if p == '.':
                continue
            elif p == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        res = ''
        if len(stack) > 0:
            for e in stack:
                res += '/' + e
        else:
            res = '/'
        return res
