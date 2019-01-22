import operator
class Solution:
    def reverse(self,x):
        s = 1
        if operator.lt(x, 0):
            s = -1
            x *= -1
        r = int(str(x)[::-1])
        if(abs(r) >= 2**31):
            return 0
        return s * r



solution = Solution()
print(solution.reverse(-123))