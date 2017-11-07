# Encode and Decode TinyURL

# double hash map; expand length

# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
#
# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

class Codec:

    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self):
        self.longToShort = {}
        self.shortToLong = {}
        self.length = 6 # initial length

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.longToShort:
            return self.longToShort[longUrl]
        for i in range(10):
            # WRONG: shortUrl = [random.choice(Codec.chars) for _ in range(self.length)]
            shortUrl = ''.join([random.choice(Codec.chars) for _ in range(self.length)])
            if not shortUrl in self.shortToLong:
                self.longToShort[longUrl] = shortUrl
                self.shortToLong[shortUrl] = longUrl
                return shortUrl
        # expand length
        self.length += 1
        shortUrl = [random.choice(Codec.chars) for _ in range(self.length)]
        self.longToShort[longUrl] = shortUrl
        self.shortToLong[shortUrl] = longUrl
        return 'http://tinyurl.com/' + shortUrl


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.shortToLong[shortUrl.split('/')[-1]]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))



# ???
class Codec:
    def __init__(self):
        self.urls = []

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.urls.append(longUrl)
        return 'http://tinyurl.com/' + self.toSixtyTwo(len(self.urls) - 1)


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.urls[self.toDec(shortUrl.split('/')[-1])]

    def toSixtyTwo(self, n):
        charSet = [chr(x + ord('0')) for x in range(10)] + [chr(x + ord('a')) for x in range(26)] + [chr(x + ord('A')) for x in range(26)]
        res = []
        while n:
            res.append(charSet[n % 62])
            n /= 62
        return ''.join(res[::-1])

    def toDec(self, s):
        res = 0
        for c in s:
            if '0' <= c <= '9':
                res += ord(c) - ord('0')
            elif 'a' <= c <= 'z':
                res += 10 + ord(c) - ord('a')
            else:
                res += 36 + ord(c) - ord('A')
            res *= 62
        return res



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
