# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        tmp = [""] *  4
        while i < n:
            x = read4(tmp)
            if x == 0:
                return i
            for j in range(x):
                buf[i + j] = (tmp[j])
            i += x
        return n
