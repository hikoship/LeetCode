# Palindrome Permutation II

# try not to copy strings

# Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.
#
# For example:
#
# Given s = "aabb", return ["abba", "baab"].
#
# Given s = "abc", return [].
#
# Hint:
#
# If a palindromic permutation exists, we just need to generate the first half of the string.
# To generate all distinct permutations of a (half of) string, use a similar approach from: Permutations II or Next Permutation.

class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        nums = [0] * 128
        oddIndex = -1
        for c in s:
            nums[ord(c)] += 1
        for i, n in enumerate(nums):
            if n % 2:
                if oddIndex != -1:
                    return []
                oddIndex = i
        nums[oddIndex] -= 1

        if oddIndex == -1:
            oddChr = ''
        else:
            oddChr = chr(oddIndex)

        array = []
        for i, n in enumerate(nums):
            array += chr(i) * (n / 2)

        res = []
        self.dfs(res, array, [])
        res = [''.join(x) for x in res]
        res = [x + oddChr + x[::-1] for x in res]

        return res

    def dfs(self, res, array, prefix):
        l = len(array)
        if l == 0:
            res.append(prefix)
        else:
            for i in range(l):
                if i == 0 or array[i] != array[i - 1]:
                    # WRONG: self.dfs(res, array[i + 1:], prefix + [array[i]])
                    self.dfs(res, array[:i] + array[i + 1:], prefix + [array[i]])
