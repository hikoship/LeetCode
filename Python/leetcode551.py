# Student Attendance Record I

# easy

# You are given a string representing an attendance record for a student. The record only contains the following three characters:
#
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
#
# You need to return whether the student could be rewarded according to his attendance record.
#
# Example 1:
# Input: "PPALLP"
# Output: True
# Example 2:
# Input: "PPALLL"
# Output: False


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        l = 0
        for c in s:
            if c == 'L':
                l += 1
                if l > 2:
                    return False
            else:
                if c == 'A':
                    a += 1
                    if a > 1:
                        return False
                l = 0
        return True
