# Remove Duplicate Letters

# add the smallest char when some char is running out of counts

# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
#
# Example:
# Given "bcabc"
# Return "abc"
#
# Given "cbacdcbc"
# Return "acdb"

# @yfcheng
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = {}
        stack = []
        visited = set()
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        for c in s:
            count[c] -= 1
            if c in visited:
                continue
            while stack and count[stack[-1]] > 0 and ord(c) < ord(stack[-1]):
                visited.remove(stack.pop())
            stack.append(c)
            visited.add(c)
        return ''.join(stack)


# @lixx2100; recursive
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.helper(s, 0, set())

    def helper(self, s, start, visited):
        count = {}
        # WRONG: pos = 0
        pos = -1
        for i in range(start, len(s)):
            c = s[i]
            if c in visited:
                continue
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        for i in range(start, len(s)):
            c = s[i]
            if c in visited:
                continue
            if pos == -1 or ord(c) < ord(s[pos]):
                pos = i
            count[c] -= 1
            if count[c] == 0:
                if pos == -1:
                    break
                # WRONG: visited.add(c)
                visited.add(s[pos])
                # WRONG: return s[pos] + self.helper(s, start + 1, visited)
                return s[pos] + self.helper(s, pos + 1, visited)
        return ''
