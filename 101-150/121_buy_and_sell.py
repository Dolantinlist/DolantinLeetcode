class Solution:
    def maxProfit(self, prices):
        l, rlt = len(prices), 0
        if l:
            minp = prices[0]
            for i in range(1, l):
                rlt = max(rlt, prices[i] - minp)
                minp = min(minp, prices[i])
        return rlt

print(Solution().maxProfit([7,6,4,3,1]))