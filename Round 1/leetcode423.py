# Reconstruct Original Digits from English

# find unique characters in digits

# Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.
#
# Note:
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
# Input length is less than 50,000.
# Example 1:
# Input: "owoztneoer"
#
# Output: "012"
# Example 2:
# Input: "fviefuro"
#
# Output: "45"

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        num = [0] * 10
        count = [0] * 26
        for c in s:
            count[ord(c) - 97] += 1
        num[0] = count[25] # z -> zero
        num[2] = count[22] # w -> two
        num[4] = count[20] # u -> four
        num[6] = count[23] # x -> six
        num[8] = count[6] # g -> eight

        num[5] = count[5] - num[4] # f -> five - four
        num[7] = count[18] - num[6] # s -> seven - six

        num[1] = count[14] - num[0] - num[2] - num[4] # o -> one - (zero + two + four)
        num[3] = count[17] - num[0] - num[4] # r -> three - (zero + four)
        num[9] = count[8] - num[5] - num[6] - num [8] # i -> nine - (five + six + eight)

        res = ''
        for i in range(10):
            res += str(i) * num[i]
        return res
