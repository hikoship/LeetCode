# Letter Combinations of a Phone Number

# backtracking: similar to combinations; iteration:

# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        a = []
        for d in digits:
            # first letter of each digit
            a.append(chr(91 + int(d) * 3 + int(int(d) > 7)))
        l = len(a)
        res = []
        while True:
            cur = l - 1
            while not a[cur] in 'cfilosvz':
                res.append(''.join(a))
                a[cur] = chr(ord(a[cur]) + 1) # next letter
            res.append(''.join(a))
            while a[cur] in 'cfilosvz':
                cur -= 1
                if cur < 0:
                    return res
            a[cur] = chr(ord(a[cur]) + 1) # next letter
            for i in range(cur + 1, l):
                a[i] = chr(ord(a[i]) - 3) if a[i] == 's'or a[i] == 'z' else chr(ord(a[i]) - 2)

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        res = ['']
        for d in digits:
            charSet = self.getCharSet(int(d))
            tmp = []
            for e in res:
                for c in charSet:
                    tmp.append(e + c)
            res = tmp
        return res

    # def getCharSet(self, d):
    #     order = 91 + int(d) * 3 + int(int(d) > 7)
    #     a = [chr(order), chr(order + 1), chr(order + 2)]
    #     if order == 112 or order == 119: # 'p' or 'w'
    #         a.append(chr(order + 3))
    #     return a

    def getCharSet(self, d):
        if d == 2:
            return ['a', 'b', 'c']
        if d == 3:
            return ['d', 'e', 'f']
        if d == 4:
            return ['g', 'h', 'i']
        if d == 5:
            return ['j', 'k', 'l']
        if d == 6:
            return ['m', 'n', 'o']
        if d == 7:
            return ['p', 'q', 'r', 's']
        if d == 8:
            return ['t', 'u', 'v']
        if d == 9:
            return ['w', 'x', 'y', 'z']
