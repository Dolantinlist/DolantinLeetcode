class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        buy1 = buy2 = - max(prices)
        sell1 = sell2 = 0
        for i in range(len(prices)):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2

print(Solution().maxProfit([3,3,5,0,0,3,1,4]))