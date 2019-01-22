class Solution:
    def maxProfit(self, prices):
        rlt = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                rlt += prices[i] - prices[i - 1]
        return rlt

print(Solution().maxProfit([7,1,5,3,6,4]))