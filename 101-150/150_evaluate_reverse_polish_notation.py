class Solution:
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t.isdigit() or t[1:].isdigit():
                stack.append(int(t))
            else:
                a = stack.pop()
                b = stack.pop()
                if t == '+':
                    c = b + a
                elif t == '-':
                    c = b - a
                elif t == '*':
                    c = b * a
                else:
                    c = int(b / a)
                stack.append(c)
        return stack.pop()

print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))