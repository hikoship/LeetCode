# Sort Transformed Array

# find vertex of the graph; mind opening direction; c doesn't matter

# Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.
#
# The returned array must be in sorted order.
#
# Expected time complexity: O(n)
#
# Example:
# nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,
#
# Result: [3, 9, 15, 33]
#
# nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5
#
# Result: [-23, -5, 1, 7]

# optimization: from two sides to center
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        # c doesn't matter the order
        res = []
        if a == 0:
            res = map(lambda x: b * x + c, nums)
            return res if b > 0 else res[::-1]
        # BUG: vertex = -b / a
        vertex = -float(b) / a / 2 # average of intersections of ax^2 + bx = 0: x = 0 and x = -b/a
        left = 0
        right = len(nums) - 1
        while left <= right:
            if vertex - nums[left] > nums[right] - vertex:
                res.append(self.calculate(nums[left], a, b, c))
                left += 1
            else:
                res.append(self.calculate(nums[right], a, b, c))
                right -= 1
        return res if a < 0 else res[::-1]

    def calculate(self, x, a, b, c):
        return a * x * x + b * x + c



class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        # c doesn't matter the order
        res = []
        if a == 0:
            res = map(lambda x: b * x + c, nums)
            return res if b > 0 else res[::-1]
        # BUG: vertex = -b / a
        vertex = -float(b) / a / 2 # average of intersections of ax^2 + bx = 0: x = 0 and x = -b/a
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if nums[mid] == vertex:
                right = mid
                break
            elif nums[mid] < vertex:
                left = mid + 1
            else:
                right = mid
        left = right - 1
        while left >= 0 and right < len(nums):
            if vertex - nums[left] > nums[right] - vertex:
                res.append(self.calculate(nums[right], a, b, c))
                right += 1
            else:
                res.append(self.calculate(nums[left], a, b, c))
                left -= 1
        while left >= 0:
            res.append(self.calculate(nums[left], a, b, c))
            left -= 1
        while right < len(nums):
            res.append(self.calculate(nums[right], a, b, c))
            right += 1
        # BUG: return res # a matters opening direction
        return res if a > 0 else res[::-1]

    def calculate(self, x, a, b, c):
        return a * x * x + b * x + c
