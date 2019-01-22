class Solution:
    def minimumTotal(self, triangle):
        l = len(triangle)
        res = triangle[-1]
        for i in range(l - 2, -1, -1):
            for j in range(i + 1):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        return res[0]