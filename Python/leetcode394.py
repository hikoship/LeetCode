# Decode String

# recursive

# Given an encoded string, return it's decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
#
# Examples:
#
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.f(s, 0, len(s) - 1)

    def f(self, s, start, end):
        res = ''
        while start <= end:
            if '0' <= s[start] <= '9':
                num = 0
                while '0' <= s[start] <= '9':
                    num = 10 * num + int(s[start])
                    start += 1

            elif 'a' <= s[start] <= 'z':
                res += s[start]
                start +=    1

            elif s[start] == '[':
                i = start + 1
                count = 1
                while True:
                    if s[i] == '[':
                        count += 1
                    elif s[i] == ']':
                        count -= 1
                        if count == 0:
                            break
                    i += 1
                res += num * self.f(s, start + 1, i - 1)
                start = i + 1
        return res
