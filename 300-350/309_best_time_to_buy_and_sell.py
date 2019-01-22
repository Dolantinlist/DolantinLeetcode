class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        l = len(prices)
        hold = [0] * l
        nhold = [0] * l
        state = [False] * l
        hold[0] = -prices[0]
        for i in range(1, l):
            nhold[i] = max(nhold[i - 1], prices[i] + hold[i - 1])
            if nhold[i] > nhold[i - 1]:
                state[i] = True
            if state[i - 1]:
                hold[i] = max(hold[i - 1], nhold[i - 2] - prices[i])
            else:
                hold[i] = max(hold[i - 1], nhold[i - 1] - prices[i])
        return nhold[-1]
print(Solution().maxProfit([1,2,3,0,2]))