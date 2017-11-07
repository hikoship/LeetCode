# Perfect Number

# ...edge cases

# We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
#
# Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
# Example:
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# Note: The input number n will not exceed 100,000,000. (1e8)

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        arr = []
        for x in range(1, int(math.sqrt(abs(num))) + 1):
            if num % x == 0:
                arr.append(x)
                if x * x != abs(num):
                    arr.append(abs(num) / x)
        return sum(arr) == 2 * num
