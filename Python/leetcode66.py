# Plus One

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        l = len(digits)

        for i in range(l):
            if digits[l - i - 1] < 9:
                digits[l - i - 1] += 1
                return digits
            else:
                digits[l - i - 1] = 0
        return [1] + digits
