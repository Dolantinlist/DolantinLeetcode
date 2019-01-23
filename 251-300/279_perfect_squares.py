import math
class Solution:
    def numSquares(self, n):
        k = [pow(c, 2) for c in range(1, int(math.sqrt(n)) + 1)]
        rlt = list(range(0, n + 1))
        for i in range(1, n + 1):
            rlt[i] = min([rlt[i - c] + 1 if i - c >= 0 else rlt[i] for c in k] + [rlt[i]])
        return rlt[n]

print(Solution().numSquares(13))