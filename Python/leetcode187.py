# Repeated DNA Sequences

# hash table

#All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
# For example,
#
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        i = 10
        res = []
        subSet = set()
        while i <= len(s):
            sub = s[i - 10 : i]
            if sub in subSet and not sub in res:
                res.append(sub)
            subSet.add(sub)
            i += 1
        return res
