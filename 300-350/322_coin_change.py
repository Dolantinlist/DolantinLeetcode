class Solution:
    def coinChang(self, coins, amount):
        MAX = float('inf')
        rlt = [0] + [MAX] * amount
        for i in range(1, amount + 1):
            rlt[i] = min([rlt[i - c] if i - c >= 0 else MAX for c in coins]) + 1
        return rlt[amount] if rlt[amount] != MAX else -1
print(Solution().coinChang([2], 3))