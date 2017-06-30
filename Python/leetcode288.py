# Unique Word Abbreviation

# abbr as key; words set as value

# An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:
#
# a) it                      --> it    (no abbreviation)
#
#      1
# b) d|o|g                   --> d1g
#
#               1    1  1
#      1---5----0----5--8
# c) i|nternationalizatio|n  --> i18n
#
#               1
#      1---5----0
# d) l|ocalizatio|n          --> l10n
# Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.
#
# Example:
# Given dictionary = [ "deer", "door", "cake", "card" ]
#
# isUnique("dear") ->
# false
#
# isUnique("cart") ->
# true
#
# isUnique("cane") ->
# false
#
# isUnique("make") ->
# true


class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.abbr = dict()
        for word in dictionary:
            key = self.getAbbr(word)
            if key in self.abbr:
                self.abbr[key].add(word)
            else:
                # WRONG: self.abbr[key] = set(word)
                self.abbr[key] = set([word])


    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        key = self.getAbbr(word)
        if not key in self.abbr:
            return True
        if word in self.abbr[key] and len(self.abbr[key]) == 1:
            return True
        return False

    def getAbbr(self, word):
        if len(word) < 3:
            return word
        else:
            return word[0] + str(len(word) - 2) + word[-1]




# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
