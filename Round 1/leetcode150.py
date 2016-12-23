class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums = []
        for token in tokens:
            if token == "+":
                nums.append(nums.pop() + nums.pop())
            elif token == "-":
                x = nums.pop() 
                y = nums.pop()
                nums.append(y - x)
            elif token == "*":
                nums.append(nums.pop() * nums.pop())
            elif token == "/":
                x = nums.pop() 
                y = nums.pop()
                nums.append(self.div(y, x))
            else:
                nums.append(int(token))
        return nums[0]

    def div(self, a, b):
        if a > 0 and b > 0 or a < 0 and b < 0:
            return a / b
        else:
            return -(abs(a) / abs(b))
            