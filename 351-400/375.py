class Solution:
    def getMoneyAmount(self, n):
        lo = 1
        hi = n
        rlt = 0
        if n < 3:
            return rlt
        while lo != hi:
            mid = (lo + hi) // 2 + 1 if (lo + hi) % 2 else (lo + hi) // 2
            rlt += mid
            lo = mid + 1
        return rlt
print(Solution().getMoneyAmount(2))
