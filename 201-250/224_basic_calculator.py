class Solution:
    def calculate(self, s: str) -> int:
        res, sign, num, stack = 0, 1, 0, []
        for ss in s:
            if ss.isdigit():
                num = 10*num + int(ss)
            elif ss in ['+', '-']:
                res += num*sign
                sign = 1 if ss == '+' else -1
                num = 0
            elif ss == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif ss == ')':
                res += num*sign
                res*= stack.pop()
                res += stack.pop()
                num = 0
        return res + num*sign

print(Solution().calculate("1+2+(3-4)"))