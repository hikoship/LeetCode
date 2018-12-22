class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.pre = {}
        self.rev = {}
        for i, w in enumerate(words):
            cur = self.pre
            if '#' not in cur:
                cur['#'] = i
            cur['#'] = max(cur['#'], i)
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
                if '#' not in cur:
                    cur['#'] = i
                cur['#'] = max(cur['#'], i)

            cur = self.rev
            if '#' not in cur:
                cur['#'] = i
            cur['#'] = max(cur['#'], i)
            for c in w[::-1]:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
                if '#' not in cur:
                    cur['#'] = i
                cur['#'] = max(cur['#'], i)


    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        p = self.pre
        for c in prefix:
            if c not in p:
                return -1
            p = p[c]

        r = self.rev
        for c in suffix[::-1]:
            if c not in r:
                return -1
            r = r[c]

        return min(p['#'], r['#'])
