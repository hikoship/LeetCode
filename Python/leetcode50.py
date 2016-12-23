# Pow(x, n)

# edge cases

# Implement pow(x, n).

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        elif x == 1:
            return 1
        elif x == -1:
            return -1 if n % 2 else 1
        elif n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2:
            return x * self.myPow(x, n / 2) ** 2
        else:
            return self.myPow(x, n / 2) ** 2
