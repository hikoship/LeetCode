# Encode and Decode Strings

# hex is slow; length + content is fast

# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
#
# Machine 1 (sender) has the function:
#
# string encode(vector<string> strs) {
#   // ... your code
#   return encoded_string;
# }
# Machine 2 (receiver) has the function:
# vector<string> decode(string s) {
#   //... your code
#   return strs;
# }
# So Machine 1 does:
#
# string encoded_string = encode(strs);
# and Machine 2 does:
#
# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.
#
# Implement the encode and decode methods.
#
# Note:
# The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
# Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
# Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.

class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        res = []
        for s in strs:
            # append separately to accelerate
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return ''.join(res)


    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        start = 0
        i = 0
        res = []
        while i < len(s):
            if s[i] == '#':
                l = int(s[start : i])
                res.append(s[i + 1: i + l + 1])
                i += l + 1
                start = i # WRONG: don't forget to update start
            else:
                i += 1
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        res = []
        for s in strs:
            for c in s:
                res.append(hex(ord(c))[2:]) # remove '0x'
            res.append(' ')
        return ''.join(res)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        res = []
        temp = []
        i = 0
        while i < len(s):
            if s[i] == ' ':
                res.append(''.join(temp))
                temp = []
                i += 1
            else:
                temp.append(chr(int(s[i] + s[i + 1], 16)))
                i += 2
        return res
