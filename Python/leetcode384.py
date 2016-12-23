# Shuffle an Array

# swapping is faster than reconstructing the array

# Shuffle a set of numbers without duplicates.
#
# Example:
#
# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
#
# // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
# solution.shuffle();
#
# // Resets the array back to its original configuration [1,2,3].
# solution.reset();
#
# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();

import random

class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type size: int
        """
        self.origin = nums


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        a = self.origin[:]
        res = []
        i = len(a) - 1
        while i >= 0:
            idx = random.randint(0, i)
            res.append(a[idx])
            a[i], a[idx] = a[idx], a[i]
            i -= 1
        return res




# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
