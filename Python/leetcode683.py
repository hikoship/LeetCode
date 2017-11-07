# O(nk), TLE
class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        blooms = set()
        for i, x in enumerate(flowers):
            if (x - k - 1 in blooms and self.noBlooms(blooms, x - k, x - 1) or
                x + k + 1 in blooms and self.noBlooms(blooms, x + 1, x + k)):
                return i + 1
            blooms.add(x)
            print i, x, blooms, x - k in blooms
        return -1

    def noBlooms(self, blooms, i, j):
        for x in range(i, j + 1):
            if x in blooms:
                return False
        return True
