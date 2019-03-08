class Solution:
    def getMoneyAmount(self, n):
        lo = 1
        hi = n
        rlt = 0
        while True:
            if hi - lo < 1:
                return rlt
            if (hi - lo) % 2:
                mid = (hi + lo)//2 + 1
            else:
                mid = (hi + lo) // 2
            rlt += mid
            lo = rlt + 1

print(Solution().getMoneyAmount(17))
