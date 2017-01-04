class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.nums = {}


    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self.nums:
            self.nums[number] = 2
        else:
            self.nums[number] = 1


    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for n in self.nums:
            if n * 2 == value and self.nums[n] == 2:
                return True
            elif n * 2 != value and value - n in self.nums:
                return True
        return False



# TLE add O(n), find O(1)
class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.nums = set()
        self.valueSet = set()


    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        for n in self.nums:
            self.valueSet.add(number + n)
        self.nums.add(number)


    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        return value in self.valueSet


# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
