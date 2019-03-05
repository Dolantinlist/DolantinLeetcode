class Solution:
    def calculate(self, s):
        if not s:
            return 0
        stack = []
        num = 0
        op = "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            if ['+', '-', '*', '/'].count(s[i]) or i == len(s) - 1:
                if op == "+":
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop()/num))

                op, num = s[i], 0
        stack.append(num)
        return sum(stack)
#  a//b是floor(a/b)
a = "14 - 3/2"
print(Solution().calculate(a))