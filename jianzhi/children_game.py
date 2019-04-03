class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0:
            return -1
        if n == 1:
            return 0
        rlt = 0
        for i in range(2, n + 1):
            rlt = (rlt+m)%i
        return rlt
print(Solution().LastRemaining_Solution(5,3))