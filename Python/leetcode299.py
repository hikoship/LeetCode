# Bulls and Cows

# one-pass solution: use array to recorde whether secret is more or guess is more

# You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.
#
# For example:
#
# Secret number:  "1807"
# Friend's guess: "7810"
# Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
# Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. In the above example, your function should return "1A3B".
#
# Please note that both secret number and friend's guess may contain duplicate digits, for example:
#
# Secret number:  "1123"
# Friend's guess: "0111"
# In this case, the 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow, and your function should return "1A1B".
# You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.#

# tricky one-pass solution in discussion
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        x, y = 0, 0
        count = [0] * 128
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                x += 1
            else:
                if count[ord(guess[i])] < 0:
                    # remaining bits for secret
                    y += 1
                if count[ord(secret[i])] > 0:
                    # remaining bits for guess
                    y += 1
                count[ord(guess[i])] += 1
                count[ord(secret[i])] -= 1
        return str(x) + 'A' + str(y) + 'B'

# my awkward solution using hashmap
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        x, y = 0, 0
        countA = {}
        countB = {}
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                x += 1
            if secret[i] in countA:
                countA[secret[i]] += 1
            else:
                countA[secret[i]] = 1
            if guess[i] in countB:
                countB[guess[i]] += 1
            else:
                countB[guess[i]] = 1
        for n in countB:
            if n in countA:
                y += min(countA[n], countB[n])
        return str(x) + 'A' + str(y - x) + 'B'
