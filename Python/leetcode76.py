# Minimum Window Substring

#       vector<int> map(128,0);
#       int counter; // check whether the substring is valid
#       int begin=0, end=0; //two pointers, one point to tail and one  head
#       int d; //the length of substring
#
#       for() { /* initialize the hash map here */ }
#
#       while(end<s.size()){
#
#           if(map[s[end++]]-- ?){  /* modify counter here */ }
#
#           while(/* counter condition */){
#
#                /* update d here if finding minimum*/
#
#               //increase begin to make it invalid/valid again
#
#               if(map[s[begin++]]++ ?){ /*modify counter here*/ }
#           }
#
#           /* update d here if finding maximum*/
#       }

# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".
#
# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".
#
# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
#

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        remainingChars = [0] * 128
        for c in t:
            remainingChars[ord(c)] += 1
        remainingNum = len(t)
        left = 0
        right = 0
        start = -1
        minLen = len(s) + 1
        while right < len(s):
            if remainingChars[ord(s[right])] > 0:
                remainingNum -= 1
            remainingChars[ord(s[right])] -= 1
            right += 1
            while remainingNum == 0:
                if minLen > right - left:
                    minLen = right - left
                    start = left
                remainingChars[ord(s[left])] += 1
                if remainingChars[ord(s[left])] > 0:
                    remainingNum += 1
                left += 1
        return '' if minLen == len(s) + 1 else s[start: start + minLen]




class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # init
        chars = {}
        diffCount = 0 # count of chars with different occurrence numbers
        for c in t:
            if c in chars:
                chars[c] -= 1
            else:
                chars[c] = -1
                diffCount += 1
        left = 0
        right = 0
        res = s + '0' # to make it longer than s

        # loop
        while right < len(s):
            if diffCount == 0:
                if s[left] in chars:
                    if right - left < len(res):
                        res = s[left : right] # update res
                    if chars[s[left]] == 0:
                        diffCount += 1 # update diffCount
                    chars[s[left]] -= 1 # update chars
                left += 1
            else:
                if s[right] in chars:
                    chars[s[right]] += 1 # update chars
                    if chars[s[right]] == 0:
                        diffCount -= 1 # update diffCount
                right += 1

        # post process
        if diffCount == 0:
            while left < len(s):
                if s[left] in chars:
                    chars[s[left]] -= 1
                    if chars[s[left]] < 0:
                        if right - left < len(res):
                            res = s[left : right]
                        break
                left += 1

        return '' if len(res) > len(s) else res
