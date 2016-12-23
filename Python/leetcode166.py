# Fraction to Recurring Decimal

# LinkedIn 2017 Summer Intern OA.
# Calculate integer first, then use a collection to store fraction.abs
# Terminate if the remainder has appeared in the collection

# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# 
# If the fractional part is repeating, enclose the repeating part in parentheses.
# 
# For example,
# 
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".
# Hint:
# 
# No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
# Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
# Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        res = ""
        if numerator > 0 and denominator < 0 or numerator < 0 and denominator > 0:
            res = "-"
            numerator = abs(numerator)
            denominator = abs(denominator)

        res += str(numerator / denominator)
        remainder = numerator % denominator
        if remainder == 0:
            return res

        res += "."

        # Use two lists
        # fraction = []
        # quotient = []
        # while not remainder in quotient:
        #     quotient.append(remainder)
        #     remainder *= 10
        #     fraction.append(str(remainder / denominator))
        #     remainder %= denominator
        #     if remainder == 0:
        #         res += "".join(fraction)
        #         return res
        # i = quotient.index(remainder)
        # res += "".join(fraction[:i]) + "(" + "".join(fraction[i:]) + ")"

        # Use map and append fraction to res when calculating
        fraction = {}
        while not remainder in fraction:
            fraction[remainder] = len(res)
            remainder *= 10
            res += str(remainder / denominator)
            remainder %= denominator
            if remainder == 0:
                return res
        i = fraction[remainder]
        return res[:i] + "(" + res[i:] + ")"
    