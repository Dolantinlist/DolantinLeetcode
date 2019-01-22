class Solution():
    def myAtoi(self, str):
        ls = list(str.strip())
        if len(ls) == 0:
            return 0
        sign = -1 if ls[0] == '-' else 1
        i = 1 if ls[0] in ['-','+'] else 0
        res = 0
        while i < len(ls) and ls[i].isdigit():
            res = 10 * res + int(ls[i])
            i += 1
        if sign == -1:
            return sign * min(2**31, res)
        else:
            return min(2**31 - 1, res)

input = "-91283472332"
solution = Solution()
print(solution.myAtoi(input))